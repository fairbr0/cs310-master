import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import StreamListener
from textblob import TextBlob
import logging
import threading

########################
#move to a config file
logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

consumer_key = 'GsW205WNzXmFrVctvboVccoJG'
consumer_secret = '40MR98nAdU59gV9pwE9gQdSFhUUubjtqcMGfhvSmx0e0CxLr50'
access_token = '1109431981-DfVfJgHmvfm2X7pZD8drz1mebQ5UwIME9cQFrXk'
access_token_secret = 'bdzKo9YSmWY9DSbmG41R6jcDdUCjIjdjVHUkRVtyzLskw'
####################

####################
#Auth stuff.
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

class WordSentiment():

    def __init__(self, word):
        self.word = word
        self.totalSentiment = 0

class TweetStreamListener(StreamListener):

    def __init__(self, wordSentiment ,api=None):
        super(TweetStreamListener, self).__init__()
        self.num_tweets = 0
        self.totalSentiment = 0
        self.wordSentiment = wordSentiment

    def on_status(self, status):
        tweet = TextBlob(status.text)
        print status.text
        print "polarity : ", tweet.sentiment.polarity

        if tweet.sentiment.polarity < 0:
            sentiment = 'negative'
        elif tweet.sentiment == 0:
            sentiment = 'neutral'
        else:
            sentiment = 'positive'

        print sentiment
        self.num_tweets += 1
        if self.num_tweets < 50:
            self.totalSentiment += float(tweet.sentiment.polarity)
            return True
        else:
            print self.totalSentiment
            self.wordSentiment.totalSentiment = self.totalSentiment
            return False

    def on_error(self, status):
        print status

class TweetStreamWorker(threading.Thread):

    def __init__(self, word):
        threading.Thread.__init__(self)
        self.word = word
        logging.debug("Starting Thread")

    def run(self):
        listener = TweetStreamListener(self.word)
        stream = Stream(auth, listener)
        stream.filter(track=[self.word.word])

def sentiment(article):
    threads = []
    sentiments = []
    for word in article.keywords:
        wordSentiment = WordSentiment(word)
        sentiments.append(wordSentiment)
        t = TweetStreamWorker(wordSentiment)
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    sentimentDict = []
    tot = 0
    for sentiment in sentiments:
        sentimentDict.append({'word': sentiment.word, 'sentiment':sentiment.totalSentiment})
        tot += sentiment.totalSentiment

    sentimentDict.append({'word' : 'TOTAL', 'sentiment' : tot})
    print (sentmientDict)
    article.sentiment = sentimentDict
