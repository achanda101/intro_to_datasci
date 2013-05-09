import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
# print type(response)
response_json = json.load(response)
result = response_json["results"]

# print len(result)
print result[14]["text"]