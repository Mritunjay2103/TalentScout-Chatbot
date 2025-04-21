# TalentScout - Intelligent Hiring Assistant

TalentScout is an AI-powered chatbot designed to assist in the initial screening of job candidates. It collects essential information and generates relevant technical questions based on the candidate's declared tech stack.

## Features

- Professional candidate interaction
- Information gathering (name, contact details, experience, etc.)
- Tech stack-based question generation
- Context-aware conversations
- Secure data handling

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd TalentScout
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Start the Streamlit application:
```bash
streamlit run main.py
```

2. Open your web browser and navigate to the provided local URL (typically http://localhost:8501)

3. Interact with the chatbot by:
   - Providing your information when prompted
   - Answering technical questions
   - Following the conversation flow

## Project Structure

- `main.py`: Main Streamlit application
- `utils.py`: Helper functions for data processing and validation
- `prompts.py`: LLM prompts for different conversation stages
- `requirements.txt`: Project dependencies
- `.env`: Environment variables (not included in repository)

## Technical Details

- Built with Streamlit for the frontend interface
- Uses OpenAI's GPT-3.5-turbo model for conversation handling
- Implements LangChain for structured conversation management
- Follows data privacy best practices

## Data Privacy

- All candidate information is handled securely
- Data is stored locally in JSON format
- No sensitive information is shared with third parties

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenAI for providing the language model
- Streamlit for the web framework
- LangChain for the conversation management tools 