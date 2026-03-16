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
python main.py "What is 25 * 12?"

python main.py "What's the weather like in New York?"
