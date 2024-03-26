from langchain_community.utilities import SerpAPIWrapper
from dotenv import load_dotenv
import os

load_dotenv()

class CustomSerpAPIWrapper(SerpAPIWrapper):
    def __init__(self, serpapi_api_key):
        super().__init__(serpapi_api_key=serpapi_api_key)

    @staticmethod
    def _process_response(res: dict) -> str:
        """Process response from SerpAPI."""
        if "error" in res.keys():
            raise ValueError(f"Got error from SerpAPI: {res['error']}")
        if "answer_box" in res.keys() and "answer" in res["answer_box"].keys():
            toret = res["answer_box"]["answer"]
        elif "answer_box" in res.keys() and "snippet" in res["answer_box"].keys():
            toret = res["answer_box"]["snippet"]
        elif (
            "answer_box" in res.keys()
            and "snippet_highlighted_words" in res["answer_box"].keys()
        ):
            toret = res["answer_box"]["snippet_highlighted_words"][0]
        elif (
            "sports_results" in res.keys()
            and "game_spotlight" in res["sports_results"].keys()
        ):
            toret = res["sports_results"]["game_spotlight"]
        elif (
            "knowledge_graph" in res.keys()
            and "description" in res["knowledge_graph"].keys()
        ):
            toret = res["knowledge_graph"]["description"]
        elif "snippet" in res["organic_results"][0].keys():
            toret = res["organic_results"][0]["link"]
        else:
            toret = "No good search result found"
        return toret


def get_profile_url(name: str):
    """Searches for Linkedin or twitter Profile Page."""
    serpapi_api_key = os.getenv("SERPAPI_API_KEY")
    search = CustomSerpAPIWrapper(serpapi_api_key)
    res = search.run(name)

    if res.startswith("https://"):
        res_parts = res.split(".", 1)
        if len(res_parts) == 2:
            res = "https://www." + res_parts[1]
    
    return res
