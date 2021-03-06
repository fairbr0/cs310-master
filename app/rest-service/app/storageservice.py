from pymongo import MongoClient
import pymongo
from bson.objectid import ObjectId

class StorageService():

    def __init__(self, config):
        self.client = MongoClient(config['host'], config['port'])
        self.db = self.client.articles

    def getArticle(self, id):
        print id
        article = self.db.articles.find_one({"_id": ObjectId(id)})
        self.db.articles.update_one({"_id" : ObjectId(id)}, {'$inc': {'count': 1}}, upsert=False)
        article['_id'] = str(article['_id'])
        return article

    def getOutletNames(self):
        outletList = self.db.articles.distinct("source")
        outletObjList = []
        for outlet in outletList:
            outletObjList.append({'name': outlet})
        outlets = {"outlets" : outletObjList}
        print (outletList)
        return outlets

    def getKeywordsGraph(self):
        articles = self.db.articles.find()
        used_words = []
        nodes = []
        links = []
        group = 0
        for article in articles:
            words = article['keywords']
            for word in words:
                if word not in used_words:
                    used_words.append(word)
                    nodes.append({"id":word, "group":group})
            for word in words:
                for _word in words[1:]:
                    links.append({'source':word, 'target':_word})
            group += 1
        return nodes, links

    def getTopRecentlyRead(self):
        articles = self.db.articles.find().sort('count', pymongo.DESCENDING).limit(5)
        articleList = []
        for article in articles:
            article['_id'] = str(article['_id'])
            articleList.append(article)
        print articleList
        return {"articles" : articleList}

    def searchOutletNames(self, query):
        outletList = self.db.articles.distinct("source")
        outletObjList = []
        for outlet in outletList:
            if outlet.lower().startswith(query):
                outletObjList.append({'name': outlet})
                continue;
            outletNameParts = outlet.split(' ');
            for part in outletNameParts:
                if part.lower().startswith(query):
                    outletObjList.append({'name': outlet})
                    break;
        outlets = {"outlets" : outletObjList}
        print (outletList)
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

    def searchKeywords(self, query):
        keywords = self.db.articles.distinct("keywords")

        keywordList = []
        for keyword in keywords:
            print query
            if keyword.lower().startswith(query):
                keywordList.append(keyword)
        return {'keywords': keywordList}

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

    def addVote(self, id, vote):
        if vote == 'True':
            self.db.articles.update_one({"_id" : ObjectId(id)}, {'$inc': {'positivevotes': 1}}, upsert=False )
        else:
            self.db.articles.update_one({"_id" : ObjectId(id)}, {'$inc': {'negativevotes': 1}}, upsert=False )
