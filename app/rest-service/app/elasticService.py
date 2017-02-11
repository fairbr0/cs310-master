from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q

class ElasticService():

    def __init__(self, config):
        self.es = Elasticsearch([{'host':config['host'], 'port':config['port']}])
