import requests
import json
 
api_key = 'xOM7Blat-aEandu_HcS_p0l01LI71bkFltgP4Ppk0yIiB2UjYGyw6nqgAt1sbCC9wtLcJ35EyzZjEsdZlk39JhZo5Bf7bHweDZaowRY6M9egK4KR_Z_QJ3T4msYTXXYx'
headers = {'Authorization': 'Bearer %s' % api_key}
 
url='https://api.yelp.com/v3/businesses/search'

# In the dictionary, term can take values like food, cafes or businesses like McDonalds
params = {'term':'seafood','location':'New York City'}

# Making a get request to the API
req=requests.get(url, params=params, headers=headers)
 
# proceed only if the status code is 200
print('The status code is {}'.format(req.status_code))
# printing the text from the response 
json.loads(req.text)
 
 