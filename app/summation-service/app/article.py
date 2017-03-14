import json

class Article():

    title = ''
    content = ''
    author = ''
    date = ''
    source = ''
    url = ''
    img_url = ''
    keywords = []
    sentiment = []
    reduction = 0

    def __init__(self, content, title=None, author=None, date=None, source=None, url=None, img_url=None):
        self.content = content
        if title is not None:
            self.title = title
            self.author = author
            self.date = date
            self.source = source
            self.url = url
            self.img_url = img_url
            self.keywords = ['Trump', 'Obama']

    def getJson(self):
        jsonString = {'title':self.title, 'content':self.content, 'author':self.author, 'date':self.date, 'source':self.source, 'url':self.url, 'keywords':self.keywords, 'reduction':self.reduction, 'count': 0, 'img_url':self.img_url}
        return jsonString
