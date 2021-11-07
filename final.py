# Importing the python libraries
import os
import requests
from dotenv import load_dotenv

# Declaring the global variables and pulling configuration settings from .env file
load_dotenv()
proxycurl_api_key = os.getenv('PROXYCURL')
sheet_best_api_url = os.getenv('SHEET_BEST_URL')
api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
profile_url = 'your_linkedin_profile_url'


def get_linkedin_profile_data(url):
    # API headers & parameter declaration for the Proxycurl API endpoint
    header_dic = {'Authorization': 'Bearer ' + proxycurl_api_key}
    params = {
        'url': url,
        'use_cache': 'if-present',
    }

    try:
        response = requests.get(api_endpoint, params=params, headers=header_dic)

        # Try Catch block that captures the API response. If response returns a 200, this is considered successful
        # if not response is not 200, this will be considered unsuccessful
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
        # Updates the Google Sheet row based upon the "position" variable with the various linkedin_data for
        # updating the first name, last name & Linkedin data column in the Google sheet
        # For more information on how Google Sheet was updated you can visit this link
        # https://docs.sheet.best/#put-patch-update-rows
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
        # Retrieves the Google Sheet data using Sheet.best API
        response = requests.get(sheet_best_api_url)  # Saves the API response as JSON into "data" variable

        if response.status_code == 200:
            data = response.json()

            print('=================Retrieve data from Google Sheet is Successful====================')
            print(data)

        else:
            print('==================Retrieve data from Google Sheet is Successful===================')

    except Exception as err:
        print({'Error: ': err.args})


# The workflow by calling the various functions
# 1) Pull Linkedin data from Proxycurl
# 2) Save and update the data into Google sheet with an existing row using Linkedin Data that was retrieved
# 3) Retrieve data from Google sheet and display the data using Sheet.best API.
live_data = get_linkedin_profile_data(profile_url)
save_linkedin_data(live_data, 0)
display_google_sheet_data()
