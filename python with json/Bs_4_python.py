import requests
from bs4 import BeautifulSoup
#Using the requests module ,we use the "get" function
#proivided to access the webpage provided as an
#argument to this function
result=reqests.get("https://www.google.com/")

#to make sure that  the website is accessible, we can
#ensure that we obtain a 200 ok response to indicate
#that the page is indeed present:
#print(result.status_code)
'''for other potential status codes you may encounter
consult the following wikipedia page:
https://en.wikipedia.org/wiki/List_of_HTTP_status_Codes
We can also check the HTTP header od the website to
verufy that we have indeed accessed the correct page:
print(result.headers)
for more information on http header and the information
on can otain from them, you may consult :
https://en.wikipedia.org/wiki/List_of_HTTP_header_fields'''