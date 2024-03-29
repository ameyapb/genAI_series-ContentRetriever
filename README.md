# Content-Retriever
![image](https://github.com/ameyapb/genAI_series-ContentRetriever/assets/67974891/4fe20e49-badb-43f5-95a2-da3e4608ff81)
<sub>(This project primarily focuses on its backend functionality. Please overlook the simplicity of the frontend. Contributions aimed at improving the frontend are highly welcome.)</sub>

## Overview
This application harnesses the power of AI-driven language models to craft engaging conversation starters and glean insights from LinkedIn profiles. Powered by the GPT-3.5 Turbo model from OpenAI, it generates concise summaries, intriguing facts, potential topics of interest, and ice breakers tailored to individuals based on their LinkedIn profiles. The application relies on a combination of Langchain, Proxycurl, and SERP API to streamline the data retrieval process, ensuring efficient and accurate analysis.

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
