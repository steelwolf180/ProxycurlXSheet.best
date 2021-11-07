import os
import requests
from dotenv import load_dotenv
load_dotenv()

proxycurl_api_key = os.getenv('PROXYCURL')
sheet_best_api_url = os.getenv('SHEET_BEST_URL')

api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
profile_url = 'https://www.linkedin.com/in/maxongzb/'


def get_linkedin_profile_data(url):
    header_dic = {'Authorization': 'Bearer ' + proxycurl_api_key}
    params = {
        'url': url,
        'use_cache': 'if-present',
    }

    response = requests.get(api_endpoint, params=params, headers=header_dic)

    data = response.json()
    print(data)

    return data


def display_google_sheet_data():
    response = requests.get(sheet_best_api_url)  # Saves the API response as JSON into "data" variable

    data = response.json()
    print(data)

    return data
