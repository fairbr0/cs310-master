import nltk
import networkx as nx
import numpy as np
import itertools
import math
import en, json


s = open('/Users/Jake/Documents/Project-Master/app/summation-service/app/stop_words.txt', 'r')
stop_words = s.read()

def getSentenceAsTokens(content):
    tokens = nltk.sent_tokenize(content)
    return tokens

def getWordsAsTokens(content):
    tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(content)
    return tokens

def normalize(tokens):
    #convert words to lower case, and then convert from plural to singular
    return [en.noun.singular(item.lower()) for item in tokens]

def wfilter(tokens, tags=['NN', 'JJ', 'NNP']):
    #filter out words by tags
    tagged = nltk.pos_tag(tokens)
    return [item[0] for item in tagged if item[1] in tags]

def removeStopWords(tokens, stop_words):
    return [item for item in tokens if item not in stop_words]

def sentenceSimilarity(s1, s2):
    t1 = getWordsAsTokens(s1)
    t2 = getWordsAsTokens(s2)

    t1 = normalize(t1)
    t2 = normalize(t2)
    if len(t1) == 0 or len(t2) == 0:
        return 0
    x = len(set(t1).intersection(t2))
    return float(x) / (math.log(len(t1)) + math.log(len(t2)))

def wordEdgeWeight(s1, s2):
    return 1.0

def buildSentenceGraph(nodes):
    gr = nx.Graph()
    gr.add_nodes_from(nodes)
    nodePairs = list(itertools.combinations(nodes, 2))

    print len(nodePairs)
    #add edges to the Graph
    for pair in nodePairs:

        s1 = pair[0]
        s2 = pair[1]
        weight = sentenceSimilarity(s1, s2)
        gr.add_edge(s1, s2, weight=weight)

    return gr

def buildWordGraph(nodes, k):
    n = k - 1
    gr = nx.Graph()
    gr.add_nodes_from(nodes)

    #add edges
    for i in range(0, len(nodes) - n):
        for j in range (i + 1, i + k):
            gr.add_edge(nodes[i], nodes[j], weight = 1.0)
    return gr

def selectSentences(sortedsentences, sentences, i):
    returnedSentences = []
    for j in range(0, len(sentences)):
        if sentences[j] in sortedsentences[:i]:
            returnedSentences.append(sentences[j])
    return returnedSentences


def getRankedKeyphrases(text):
    tokens = getWordsAsTokens(text)
    originalTokens = tokens
    tokens = removeStopWords(tokens, stop_words)
    tokens = normalize(tokens)
    tokens = wfilter(tokens)

    graph = buildWordGraph(tokens, 2)

    #get the pagerank of each word
    calculated_page_rank = nx.pagerank(graph, weight='weight')
    return sorted(calculated_page_rank, key=calculated_page_rank.get, reverse=True)

def getRankedSentences(text):
    tokens = getSentenceAsTokens(text)
    graph = buildSentenceGraph(tokens)
    calculated_page_rank = nx.pagerank(graph, weight="weight")

    return calculated_page_rank

def getReduction(original, new):
    originalLength = len(getWordsAsTokens(original))
    newLength = len(getWordsAsTokens(new))
    print originalLength, newLength
    return 1.0 - (float(newLength) / float(originalLength))

def summarize(article):

    article.keywords = getRankedKeyphrases(article.content)[:10]
    rankedSentences = getRankedSentences(article.content)

    for i in rankedSentences:
        sentenceTokens = getWordsAsTokens(i)
        sentenceTokens = normalize(sentenceTokens)
        for j in range(0, len(article.keywords)):
            if article.keywords[j] in sentenceTokens:
                rankedSentences[i] += 0.1
    sortedSentences = sorted(rankedSentences, key=rankedSentences.get, reverse=True)

    selectedSentences = selectSentences(sortedSentences, getSentenceAsTokens(article.content), 5)


    string = ''
    for sentence in selectedSentences:
        string += sentence + "\n\n"
    reduction = getReduction(article.content, string)
    article.reduction = reduction
    article.content = string
    print (string, reduction, article.keywords)
    #apply sentiment boosts
    #reorder by keywords

def summarizeTest(content):
    keywords = getRankedKeyphrases(content)[:10]
    rankedSentences = getRankedSentences(content)

    for i in rankedSentences:
        sentenceTokens = getWordsAsTokens(i)
        sentenceTokens = normalize(sentenceTokens)
        for j in range(0, len(keywords)):
            if keywords[j] in sentenceTokens:
                rankedSentences[i] += 0.1

    sortedSentences = sorted(rankedSentences, key=rankedSentences.get, reverse=True)

    selectedSentences = selectSentences(sortedSentences, getSentenceAsTokens(content), 5)


    string = ''
    for sentence in selectedSentences:
        string += sentence + "\n\n"
    reduction = getReduction(content, string)
    return string, reduction, keywords

def getArticle(name):
    f = open(name, 'r')
    article = f.read()
    return article
