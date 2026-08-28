# LLM Starter Project

A Python application for interacting with LLMs using the Google GenAI SDK.

## Features
- Interactive terminal chat loop with memory.
- Single prompt execution via CLI arguments.
- Clean environment variable handling.

## Prerequisites
- Python 3.9+
- A Google Gemini API key from [Google AI Studio](https://aistudio.google.com/)

## Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
   cd YOUR_REPOSITORY_NAME
Set up virtual environment:

bash


python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:Install dependencies:

bash


pip install -r requirements.txt
source venv/bin/activateConfigure environment variables:

Copy .env.example to .env:
bash


cp .env.example .env
Open .env and paste your GEMINI_API_KEY.Run the application:

Interactive mode:
bash


python app.py
Single prompt mode:
bash


python app.py "What is quantum computing?"
