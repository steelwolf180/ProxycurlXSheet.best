import os
import requests
from dotenv import load_dotenv
load_dotenv()

proxycurl_api_key = os.getenv('PROXYCURL')
api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
profile_url = 'https://www.linkedin.com/in/maxongzb/'

header_dic = {'Authorization': 'Bearer ' + proxycurl_api_key}
params = {
    'url': profile_url,
    'use_cache': 'if-present',
}

response = requests.get(api_endpoint, params=params, headers=header_dic)

data = response.json()
print(data)
