import os
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from third_parties.linkedin import scrape_linkedin_profile

load_dotenv()

if __name__ == '__main__':
    print('Hello!')
    key = os.environ.get('OPENAI_API_KEY')

    summary_template = """
    Given the LinkedIn information {information} about a person I want you to create:
    1. A short Summary
    2. Two intresting facts about them
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)
    
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    
    # linkedin_data = scrape_linkedin_profile(linkendin_profile_url="//any URL")
    linkedin_data = scrape_linkedin_profile()

    # res_final = chain.invoke(input={"information": linkedin_data})
    print(chain.run(information=linkedin_data))