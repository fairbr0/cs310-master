from elasticsearch import Elasticsearch

class ElasticService():

    def __init__(self, config):
        self.es = Elasticsearch([{'host':config['host'], 'port':config['port']}])

    def postArticle(article):
        return
