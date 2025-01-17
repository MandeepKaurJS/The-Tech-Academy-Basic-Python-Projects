import requests
import json
 
api_key = 'xOM7Blat-aEandu_HcS_p0l01LI71bkFltgP4Ppk0yIiB2UjYGyw6nqgAt1sbCC9wtLcJ35EyzZjEsdZlk39JhZo5Bf7bHweDZaowRY6M9egK4KR_Z_QJ3T4msYTXXYx'
headers = {'Authorization': 'Bearer %s' % api_key}
 
url = 'https://api.yelp.com/v3/businesses/search'
params = {'term':'seafood','location':'New York City'}
 
req = requests.get(url, params=params, headers=headers)
 

parsed = json.loads(req.text)
 
businesses = parsed["businesses"]
 
for business in businesses[:10]:
    print("Name:", business["name"])
    print("Rating:", business["rating"])
    print("Address:", " ".join(business["location"]["display_address"]))
    print("Phone:", business["phone"])
    print("\n")
 
    id = business["id"]
 
    url="https://api.yelp.com/v3/businesses/" + id + "/reviews"
 
    req = requests.get(url, headers=headers)
 
    parsed = json.loads(req.text)
 
    reviews = parsed["reviews"]
 
    print("--- Reviews ---")
 
    for review in reviews:
        print("User:", review["user"]["name"], "Rating:", review["rating"], "Review:", review["text"], "\n")
 
