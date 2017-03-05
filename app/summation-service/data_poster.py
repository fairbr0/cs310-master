import urllib2
import json

with open('resources/articles/article1.json') as json_data:
    d = json.load(json_data)
    print(d)
