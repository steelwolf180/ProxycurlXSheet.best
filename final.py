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

    try:
        response = requests.get(api_endpoint, params=params, headers=header_dic)
        if response.status_code == 200:
            data = response.json()

            print('======================Retrieve Data from Linkedin is Successful===================')
            return data

        else:
            print('======================Retrieve Data from Linkedin is Unsuccessful==================')
            return {'first_name': '', 'last_name': ''}

    except Exception as err:
        print({'Error: ': err.args})


def save_linkedin_data(linkedin_data, position):
    try:
        response = requests.patch(f'{sheet_best_api_url}/{position}',
                                  json={
                                      'First Name': linkedin_data['first_name'],
                                      'Last Name': linkedin_data['last_name'],
                                      'LinkedIn Page': 'https://www.linkedin.com/in/maxongzb/',
                                      'Linkedin Data': linkedin_data}
                                  )

        if response.status_code == 200:
            print('=================Saving data to Google Sheet is Successful====================')

        else:
            print('=================Saving data to Google Sheet is Unsuccessful==================')

    except Exception as err:
        print({'Error: ': err.args})


def display_google_sheet_data():
    try:
        response = requests.get(sheet_best_api_url)  # Saves the API response as JSON into "data" variable

        if response.status_code == 200:
            data = response.json()

            print('=================Retrieve data from Google Sheet is Successful====================')
            print(data)

        else:
            print('==================Retrieve data from Google Sheet is Successful===================')

    except Exception as err:
        print({'Error: ': err.args})


live_data = get_linkedin_profile_data(profile_url)
save_linkedin_data(live_data, 0)
display_google_sheet_data()
