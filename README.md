# Google ADK: FAQ & Weather Agent

A simple AI agent built using the Google Agent Development Kit (ADK).
It can answer math and general questions using an AI model, and it can use a tool to get weather information.
The agent decides when to answer directly and when to use the tool, and it always returns the result in a clear JSON format.

## 🛠️ Setup Instructions

### 1. Prerequisites
- Python 3.11
- A Google Gemini API Key (from [Google AI Studio](https://aistudio.google.com/))

### 2. Installation
Clone this repository and navigate to the faq_agent_adk folder:

python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

Create `.env` and add `GOOGLE_API_KEY=your_key`


### Test


python main.py "What's the weather like in New York?"

<img width="613" height="154" alt="image" src="https://github.com/user-attachments/assets/eb193c12-c34a-401f-9d8a-ea78c3437ea3" />


python main.py "What is 25 * 12?"

<img width="578" height="84" alt="image" src="https://github.com/user-attachments/assets/c297ddec-a47e-4c83-87eb-c9f37e5a3fe8" />

