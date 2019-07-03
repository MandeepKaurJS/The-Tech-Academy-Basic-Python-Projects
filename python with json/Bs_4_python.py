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
#Get all necessary information from the IMDb webpage (title, link, cast)
#print(soup).get_text()
##all_movies=soup.find_all('table',class_='chart full-width')
#print(all_movies)
imdb = []
poster=[]
ratings=[]
watchinglist=[]
for container in movies[:5]:
	
    #title
	title=container.find('td',class_='titleColumn').get_text()
	imdb.append(title)
       
	#poster or image
	poster_col=container.td.a.img
	poster.append(poster_col)
      
	#ratings
	rating=container.find_all('td',class_='ratingColumn imdbRating')
	ratings.append(rating)
    #watchingList
   
	watchlist=container.find_all('td',class_='watchlistColumn')
	watchinglist.append(watchlist)
print(imdb)
print(poster)
print((ratings))
print(watchinglist)
        
        
'''movies = soup.select('td.titleColumn')
poster=soup.select('td.posterColumn')


#creating list to store movie titles

# Store each item into dictionary (data), then put those into a list (imdb)
for index in movies[:5]:
		print(index)
for index in poster[:5]:
		print(index)'''

