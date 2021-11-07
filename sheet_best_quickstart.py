# importing of python libraries
import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Loads the .env configuration as part of your environment variables
sheet_best_connection_URL = os.getenv('SHEET_BEST_URL')  # The API key from Proxycurl

data = requests.get(sheet_best_connection_URL)  # Saves the API response as JSON into "data" variable
print(data.json())
