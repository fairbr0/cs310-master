from time import gmtime, strftime
from elasticservice import ElasticService
from article import Article
import threading
import logging
logging.basicConfig(level=logging.DEBUG)
import summarize
import sentiment
import Queue

class AnalysisWorker(threading.Thread):

    def __init__(self, queue, es):
        threading.Thread.__init__(self)
        self.queue = queue
        self.es = es
        logging.debug('Created Worker Thread')

    def run(self):
        while True:
            logging.debug('Waiting for article from Queue')
            article = self.queue.get()
            logging.debug('Got article from Queue')
            summarize.summarize(article)
            sentiment.sentiment(article)
            self.es.postArticle(article)
            logging.debug('Posted article to ES')

class AnalysisEngine():

    def __init__(self, elasticService):

        self.elasticService = elasticService
        self.inputQueue = Queue.Queue()
        self.worker = self.startWorkers()

    def startWorkers(self):
        t = AnalysisWorker(self.inputQueue, self.elasticService)
        t.start()
        return t

    def close(self):
        self.inputQueue.join()
        self.worker.join()

    def inputDocument(self, request):
        article = self.constructArticle(request)
        self.inputQueue.put(article)
        logging.debug('Added request to input queue')

    def constructArticle(self, request):
        title=request.form['title']
        author=request.form['author']
        content=request.form['content']
        source=request.form['source']
        url=request.form['url']
        date = strftime("%Y-%m-%d %H:%M:%S", gmtime())

        article = Article(title, content, author, date, source, url)

        return article
