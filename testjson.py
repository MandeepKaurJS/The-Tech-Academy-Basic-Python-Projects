from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import re
import json

# Download IMDB's Top 250 data
url = 'http://www.imdb.com/chart/top'
req=requests.get(url, params=params, headers=headers)
#response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
print(response.json())