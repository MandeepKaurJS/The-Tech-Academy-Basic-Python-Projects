from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer)')
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img', {'src':re.compile('.jpg')})
for image in images: 
    print(image['src']+'\n')
 #soup = BeautifulSoup(data, 'html.parser')
    #images=soup.find(id="albumArt")
    #art_items = images.find_all(id_="podcast")
    #for image in art_items:
        #print(images.prettify())