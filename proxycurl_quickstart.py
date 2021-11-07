import os
import requests
from dotenv import load_dotenv
load_dotenv()

proxycurl_api_key = os.getenv('PROXYCURL')
api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/company/employees/'
company_url = 'https://www.linkedin.com/company/streamlit/'

header_dic = {'Authorization': 'Bearer ' + proxycurl_api_key}
params = {
    'employment_status': 'current',
    'url': company_url,
}

response = requests.get(api_endpoint, params=params, headers=header_dic)

data = response.json()
print(data)
