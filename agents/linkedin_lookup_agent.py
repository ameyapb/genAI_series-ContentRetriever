from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.tools import Tool
from tools.tools import get_profile_url
from dotenv import load_dotenv
import os

load_dotenv()

key = os.environ.get('SERP_API_KEY')

from langchain.agents import initialize_agent, Tool, AgentType

def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    template = """given the full name {name_of_person} I want you to get it me a link to their LinkedIn profile page.
                You answer should contain only a URL. The URL must start from https://www.linkedin.com
                Here are some examples for you:
                1. https://www.linkedin.com/in/ameyapb/
                2. https://www.linkedin.com/in/karan-yadav-b0b960204/
                3. https://www.linkedin.com/in/rahul-dogra-6987b2119/
                """
    
    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )
    
    tools_for_agent = [Tool(
                            name="Crawl Google for Linkedin profile page", 
                            func=get_profile_url, 
                            description="useful when you need to get the linkedin page URL"
                            )]
    
    react_prompt = hub.pull("hwchase17/react")

    agent = create_react_agent(tools=tools_for_agent, llm=llm, prompt=react_prompt)

    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(input={"input": prompt_template.format_prompt(name_of_person=name)})

    linked_profile_url = result["output"]
    
    return linked_profile_url