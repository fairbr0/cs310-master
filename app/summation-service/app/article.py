import json

class Article():

    def __init__(self, title, content, author, date, source, url):
        self.title = title
        self.content = content
        self.author = author
        self.date = date
        self.source = source
        self.url = url
        self.keywords = []

    def getJson(self):
        jsonString = {'title':self.title, 'content':self.content, 'author':self.author, 'date':self.date, 'source':self.source, 'url':self.url, 'keywords':self.keywords}
        return jsonString
