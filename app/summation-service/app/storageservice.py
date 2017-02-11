#import mongo connector
from pymongo import MongoClient

class StorageService():

    def __init__(self, config):
        self.client = MongoClient(config['host'], config['port'])
        self.db = self.client.articles
        self.article_table = self.db.articles

    def postArticle(self, article):
        request = article.getJson()
        id = self.article_table.insert_one(request).inserted_id
        #resp = self.es.index(index='articles', doc_type='article', body=request)
        #insert into mongo
        print id
        return
