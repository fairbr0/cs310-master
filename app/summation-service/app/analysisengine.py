from time import gmtime, strftime
from elasticservice import ElasticService
from article import Article
import threading
import logging
logging.basicConfig(level=logging.DEBUG)
import summarize
import sentiment

class AnalysisEngine():

    def __init__(self, elasticService):
        self.elasticService = elasticService
        self.inputQueue = []
        self.startWorkers();

    def startWorkers(self):
        

    def analysisWorker(self):
        article = constructArticle(request)
        summarize(article)
        sentiment(article)
        es.postArticle(article)

    def inputDocument(self, request):
        self.inputQueue.append(request)
        logging.debug('Added request to input queue')

    def constructArticle(request):
        title=request.form['title']
        author=request.form['author']
        content=request.form['content']
        source=request.form['source']
        url=request.fomrm['url']
        date = strftime("%Y-%m-%d %H:%M:%S", gmtime())

        article = Article(title, content, author, date, source, url)

        return article
