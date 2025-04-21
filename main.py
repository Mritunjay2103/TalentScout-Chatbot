import streamlit as st
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
import json
from typing import Dict, List

# Load environment variables
load_dotenv()

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "candidate_info" not in st.session_state:
    st.session_state.candidate_info = {
        "name": "",
        "email": "",
        "phone": "",
        "experience": "",
        "position": "",
        "location": "",
        "tech_stack": []
    }

if "current_stage" not in st.session_state:
    st.session_state.current_stage = "greeting"

# Predefined questions and responses
QUESTIONS = {
    "greeting": "Hello! Welcome to TalentScout. I'll help you through the initial screening process. What's your name?",
    "name": "Great! What's your email address?",
    "email": "Thank you. What's your phone number?",
    "phone": "How many years of experience do you have?",
    "experience": "What position are you interested in?",
    "position": "Where are you currently located?",
    "location": "What's your tech stack? (Please list programming languages, frameworks, databases, and tools you're proficient in)",
    "tech_stack": "Thank you for providing your information. Let me ask you some technical questions based on your tech stack."
}

TECH_QUESTIONS = {
    "Python": [
        "What are Python decorators and how would you use them?",
        "Explain the difference between lists and tuples in Python.",
        "How do you handle exceptions in Python?"
    ],
    "JavaScript": [
        "What is the difference between let, const, and var?",
        "Explain the concept of closures in JavaScript.",
        "What is the event loop in JavaScript?"
    ],
    "Java": [
        "What is the difference between an interface and an abstract class?",
        "Explain the concept of multithreading in Java.",
        "What are Java generics and how do you use them?"
    ],
    "SQL": [
        "What is the difference between INNER JOIN and LEFT JOIN?",
        "Explain database normalization.",
        "What are indexes and how do they improve query performance?"
    ]
}

# System prompt for the chatbot
SYSTEM_PROMPT = """You are TalentScout, an intelligent hiring assistant chatbot. Your role is to:
1. Greet candidates professionally
2. Collect essential information in this order:
   - Full Name
   - Email Address
   - Phone Number
   - Years of Experience
   - Desired Position(s)
   - Current Location
   - Tech Stack (programming languages, frameworks, databases, tools)
3. Generate relevant technical questions based on their tech stack
4. Maintain conversation context
5. End the conversation gracefully when appropriate

Always be professional, friendly, and maintain a conversational tone.
Ask for one piece of information at a time.
Validate the responses before moving to the next question.
For tech stack, ask them to list their technologies separated by commas.
After collecting tech stack, generate 3-5 technical questions for each technology they've listed.
The questions should be relevant, vary in difficulty, and test both theoretical knowledge and practical experience."""

def get_next_question():
    stages = list(QUESTIONS.keys())
    current_index = stages.index(st.session_state.current_stage)
    if current_index < len(stages) - 1:
        return stages[current_index + 1]
    return None

def generate_tech_questions(tech_stack: List[str]) -> List[str]:
    questions = []
    for tech in tech_stack:
        if tech in TECH_QUESTIONS:
            questions.extend(TECH_QUESTIONS[tech])
    return questions

def init_chat_model():
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        
        return ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0.7,
            api_key=api_key
        )
    except Exception as e:
        st.error(f"Error initializing chat model: {str(e)}")
        return None

def main():
    st.title("TalentScout - Intelligent Hiring Assistant")
    
    # Initialize chat model
    chat_model = init_chat_model()
    if not chat_model:
        st.error("Failed to initialize the chat model. Please check your API key and try again.")
        return
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Type your message here..."):
        try:
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # Display user message
            with st.chat_message("user"):
                st.write(prompt)
            
            # Generate assistant response
            with st.chat_message("assistant"):
                # Prepare messages for the model
                messages = [
                    SystemMessage(content=SYSTEM_PROMPT),
                    *[HumanMessage(content=msg["content"]) for msg in st.session_state.messages]
                ]
                
                # Get response from the model
                response = chat_model.invoke(messages)
                
                # Display assistant response
                st.write(response.content)
                
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response.content})
                
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.info("Please try again or check your API key and internet connection.")

if __name__ == "__main__":
    main() 