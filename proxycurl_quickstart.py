# importing of python libraries
import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Loads the .env configuration as part of your environment variables
proxycurl_api_key = os.getenv('PROXYCURL')  # The API key from Proxycurl

# Proxycurl API endpoint called "LinkedIn Person Profile".
# For more details of the API - https://nubela.co/proxycurl/docs#people-api-linkedin-person-profile-endpoint
api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
profile_url = 'https://www.linkedin.com/in/maxongzb/'   # The LinkedIn profile url you want to get more information with

# The header & parameter configuration of the API request
headers = {'Authorization': 'Bearer ' + proxycurl_api_key}
params = {'url': profile_url, 'use_cache': 'if-present'}

# The calling the API using request and save it into response
response = requests.get(api_endpoint, params=params, headers=headers)

data = response.json()  # Saves the API response as JSON into "data" variable
print(data)
