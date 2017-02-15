from pymongo import MongoClient
import pymongo

class StorageService():

    def __init__(self, config):
        self.client = MongoClient(config['host'], config['port'])
        self.db = self.client.articles

    def getOutletNames(self):
        outletList = self.db.articles.distinct("source")
        outlets = {"outlets" : outletList}
        return outlets

    def getOutletArticles(self, outlet, id=None):
        if id is None:
            id = 0
        articles = self.db.articles.find({"source":outlet}).sort('date', pymongo.DESCENDING).skip(id).limit(20)
        articleList = []
        for article in articles:
            article['_id'] = str(article['_id'])
            articleList.append(article)
        print articleList
        return {"articles" : articleList, "id":id + 20}

    def getKeywords(self):
        keywordsList = self.db.articles.distinct("keywords")
        keywords = {"keywords" : keywordsList}
        return keywords

    def getKeywordArticles(self, keyword, id=None):
        if id is None:
            id = 0
        articles = self.db.articles.find({"keywords": keyword }).sort('date', pymongo.DESCENDING).skip(id).limit(20)
        articleList = []
        for article in articles:
            article['_id'] = str(article['_id'])
            articleList.append(article)
        print articleList
        return {"articles" : articleList, "id":id + 20}

    def getRecent(self, id=None):
        if id is None:
            id = 0
        articles = self.db.articles.find().sort('date', pymongo.DESCENDING).skip(id).limit(20)
        articleList = []
        for article in articles:
            article['_id'] = str(article['_id'])
            articleList.append(article)
        print articleList
        return {"articles" : articleList, "id":id + 20}

    def getRecentByOutlets(self, outlets, id=None):
        if id is None:
            id = 0
        articles = self.db.articles.find({'source' : {'$in': outlets}}).sort('date', pymongo.DESCENDING).skip(id).limit(20)
        articleList = []
        for article in articles:
            article['_id'] = str(article['_id'])
            articleList.append(article)
        print articleList
        return {"articles" : articleList, "id":id + 20}
