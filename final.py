import os
import requests
from dotenv import load_dotenv
load_dotenv()

proxycurl_api_key = os.getenv('PROXYCURL')
sheet_best_api_key = os.getenv('SHEET_BEST')

api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/company/employees/'
company_url = 'https://www.linkedin.com/company/streamlit/'


def get_linkedin_data(url):
    header_dic = {'Authorization': 'Bearer ' + proxycurl_api_key}
    params = {
        'employment_status': 'current',
        'url': url,
    }
    response = requests.get(api_endpoint,
                            params=params,
                            headers=header_dic)
    print(response.json())

    return response.json()

