from django.shortcuts import render

import requests
import re
from bs4 import BeautifulSoup
import requests
import re

# Download IMDB's Top 250 data
url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
movies = soup.find_all('table',class_='chart full-width')
for link in movies.findAll('td',class_='titleColumn'):
    title=link.find('a')
    print(title.get_text('title'))
