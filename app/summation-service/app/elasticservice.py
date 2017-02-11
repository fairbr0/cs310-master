from elasticsearch import Elasticsearch

class ElasticService():

    def __init__(self, config):
        self.es = Elasticsearch([{'host':config['host'], 'port':config['port']}])

    def postArticle(self, article):
        request = article.getJson()
        resp = self.es.index(index='articles', doc_type='article', body=request)
        print resp
        return
