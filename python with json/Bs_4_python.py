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
#Get all necessary information from the IMDb webpage (title, link, cast)
movies = soup.select('td.titleColumn')+soup.select('td.posterColumn')


#creating list to store movie titles

# Store each item into dictionary (data), then put those into a list (imdb)
for index in movies:
		print(index)

