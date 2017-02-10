import requests
from elasticsearch import Elasticsearch
import json

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
res = requests.get('http://localhost:9200')
r = requests.get('http://swapi.co/api/people/'+ str(0))


print es.get(index='sw', doc_type='people', id=1)
