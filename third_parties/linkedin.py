import os
import requests

def scrape_linkedin_profile(linkendin_profile_url: str = None):
    """scrape information from LinkedIn Profiles,
    Manually scrape the information from the LinkedIn profile"""
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}

    # Uncomment if you want to go-live with proxyURL API. Please note you need to have credits to use this. 
    # response = requests.get(
    #     api_endpoint, params={"url": linkendin_profile_url}, headers=header_dic
    # )

    # This is a free sample response
    response = requests.get("https://gist.githubusercontent.com/ameyapb/7318c844d3838cb28f2868464d8e75ed/raw/3ac181653397f90e2d527b992a02a320af01d9c1/johnrmarty.json")

    data = response.json()

    #cleaning data to remove empty feilds.
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
            and k not in ["people_also_viewed", "certifications"]
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data