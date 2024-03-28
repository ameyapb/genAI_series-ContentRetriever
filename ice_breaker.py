from typing import Tuple
import os
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from output_parsers import person_intel_parsor, PersonIntel

load_dotenv()

def ice_breaker(name: str) -> Tuple[PersonIntel, str]:
    key = os.environ.get('OPENAI_API_KEY')

    summary_template = """
    Given the LinkedIn information {information} about a person I want you to create:
    1. A short Summary
    2. Two intresting facts about them
    3. A topic that may interest them
    4. 2 creative Ice Breakers to open a conversation with them
    \n{format_instructions}
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], 
                                             template=summary_template,
                                             partial_variables={"format_instructions": person_intel_parsor.get_format_instructions()})
    
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    
    linkedin_profile_url = linkedin_lookup_agent(name=name)

    """ Uncomment the below linkedin_profile_url to pass linkedin URL to scrape_linkedin_profile(). Please note you will also 
        need to make changes to linkedin.py. Currently we are testing on standard sample response."""
    linkedin_data = scrape_linkedin_profile(
        linkendin_profile_url=linkedin_profile_url
    )

    result = chain.run(information=linkedin_data)
    print(person_intel_parsor.parse(result))
    print(linkedin_profile_url)
    print(linkedin_data.get("profile_pic_url"))
    return person_intel_parsor.parse(result), linkedin_data.get("profile_pic_url")

if __name__ == '__main__':
    print('Hello!')
    ice_breaker(name="Ameya Patil IBM")
    