# Introduction
This is the repo for the use of [ProxyCurl](https://nubela.co/proxycurl/) an API service to pull data from LinkedIn
and [Sheet.best](https://sheet.best/) that acts as the **middle man** to save the data 
from [LinkedIn](https://www.linkedin.com/) into a [Google Sheet](https://www.google.com/sheets/about/) file.

Please refer to the article called
"[Lead Generation from ProxyCurl into Sheet.best with Python - Reading Time 10 Mins]()" 
and the YouTube video called "[Lead Generation from ProxyCurl into Sheet.best with Python]()"
for more information how to use execute the various program.

# Project Structure
* `README.md` - Details on how to set up and run the various programs in the repo
* `final.py` - The integration of both Proxycurl and Sheet.best to save the data into a Google Sheet
* `proxycurl_quickstart.py` - Proxycurl quickstart program
* `requirements.txt` - Your python packages needed for this article
* `sheet_best_quickstart.py` - Sheet.best quickstart program
* `venv` - The name of your virtual environment 
* `.env` - Contains the API keys for Proxycurl and Sheet.best API URL

# Setup
* Create a virtual environment called "venv"
```commandline
python3 -m venv env
```
* Enable your newly created virtual environment `venv`
```commandline
source venv/bin/activate
```
* Install the various python libraries in your `venv` using `requirements.txt` file.
```commandline
pip install -r requirement.txt
```
