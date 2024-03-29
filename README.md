# Content-Retriever

## Overview
This application leverages AI-powered language models to generate conversation starters and insights based on LinkedIn profiles. It utilizes GPT-3.5 Turbo model from OpenAI to generate summaries, interesting facts, topics of interest, and ice breakers for individuals based on their LinkedIn profiles along with Langchain.

## Installation
1. Clone this repository:
```
git clone https://github.com/your_repository.git
```
2. Navigate to the project directory:
```
cd your_repository
```
3. Install the required dependencies:
```
pip install -r requirements.txt
```
4. Set up environment variables by creating a `.env` file in the root directory:
```
OPENAI_API_KEY=
PROXYCURL_API_KEY=
SERPAPI_API_KEY=
```
5. Run the FLASK app via:
```
python app.py
```