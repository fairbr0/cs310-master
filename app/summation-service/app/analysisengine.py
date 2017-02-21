from time import gmtime, strftime
from storageservice import StorageService
from article import Article
import threading
import logging
logging.basicConfig(level=logging.DEBUG)
import summarize
import sentiment
import Queue

class AnalysisWorker(threading.Thread):

    def __init__(self, queue, ss):
        threading.Thread.__init__(self)
        self.queue = queue
        self.ss = ss
        logging.debug('Created Worker Thread')

    def run(self):
        while True:
            logging.debug('Waiting for article from Queue')
            article = self.queue.get()
            logging.debug('Got article from Queue')
            summarize.summarize(article)
            #sentiment.sentiment(article)
            self.ss.postArticle(article)
            logging.debug(article.content, article.keywords)
            logging.debug('Posted article to ES')

class AnalysisEngine():

    def __init__(self, storageService):

        self.storageService = storageService
        self.inputQueue = Queue.Queue()
        self.worker = self.startWorkers()

    def startWorkers(self):
        t = AnalysisWorker(self.inputQueue, self.storageService)
        t.start()
        return t

    def close(self):
        self.inputQueue.join()
        self.worker.join()

    def inputDocument(self, request):
        article = self.constructArticle(request)
        self.inputQueue.put(article)
        logging.debug('Added request to input queue')

    def returnDocument(self, request):
        article = self.constructBareArticle(request)
        summarize.summarize(article)
        #sentiment.sentiment(article)
        return article.getJson()

    def constructArticle(self, request):
        title=request.form['title']
        author=request.form['author']
        content=request.form['content']
        source=request.form['source']
        url=request.form['url']
        date = strftime("%Y-%m-%d %H:%M:%S", gmtime())

        article = Article(content, title, author, date, source, url)

        return article

    def constructBareArticle(self, request):
        content = request.form['content']
        article = Article(content)
        return article
