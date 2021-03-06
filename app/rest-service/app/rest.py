from flask import Flask, jsonify
from flask import abort, make_response, request
from flask.ext.httpauth import HTTPBasicAuth
from flask_cors import CORS, cross_origin

auth = HTTPBasicAuth()
from app import app
import config
import logging
from storageservice import StorageService
logging.basicConfig(level=logging.DEBUG)

ss = StorageService(config.dbAddr)

CORS(app)

@app.route('/alive', methods=['GET'])
def alive():
    return jsonify({'msg':'success'}), 200

#returns a list of news outlets
@app.route('/outlets', methods=['GET'])
def getOutlets():
    return jsonify(ss.getOutletNames()), 200

#return a list of articles from the selected news outlets
@app.route('/outlet/<outlet>', methods=['GET'])
@app.route('/outlet/<outlet>/<int:id>', methods=['GET'])
def getOutletArticles(outlet, id=None):
    logging.debug(outlet)
    if id is not None:
        logging.debug(id)
    result = ss.getOutletArticles(outlet, id)
    return jsonify({'response':result}), 200

#return a list of top keywords
@app.route('/keywords', methods=['GET'])
def getKeywords():
    return jsonify({'response':ss.getKeywords()}), 200

#returns a list of articles with selected keyword
@app.route('/keywords/<keyword>', methods=['GET'])
@app.route('/keywords/<keyword>/<int:id>', methods=['GET'])
def getKeywordArticles(keyword, id=None):
    logging.debug(keyword)
    if id is not None:
        logging.debug(id)
    result = ss.getKeywordArticles(keyword, id)
    return jsonify({'response':result}), 200

@app.route('/keywords_graph', methods=['GET'])
def getKeywordsGraph():
    nodes, links = ss.getKeywordsGraph()
    resp = {'nodes': nodes, 'links' : links}
    return jsonify({'response':resp}), 200

@app.route('/article/<string:id>')
def getArticle(id):
    result = ss.getArticle(id)
    return jsonify({'response':result}), 200

#returns a list of most recent
@app.route('/getrecent', methods=['GET'])
@app.route('/getrecent/<int:id>', methods=['GET'])
def getTopArticlesNext(id=None):
    if id is not None:
        logging.debug(id)
    result = ss.getRecent(id)
    return jsonify({'response':result}), 200

#returns list of most recent from chosen outlets
@app.route('/getrecentoutlet/<int:id>', methods=['GET'])
def getTopArticlesOutlets(id=None):
    logging.debug(request.args)
    outlets = request.args.getlist('outlet')
    if id is not None:
        logging.debug(id)
    result = ss.getRecentByOutlets(outlets, id)
    return jsonify({'response':result}), 200
    #return jsonify({'msg':'success'}), 200

@app.route('/keywordsearch/<string:query>', methods=['GET'])
def searchForKeyword(query):
    matches = ss.searchKeywords(query)
    return jsonify({'response' : matches})

@app.route('/outletsearch', methods=['GET'])
def searchForOutlet():
    query = request.args.get('query')
    matches = ss.searchOutletNames(query)
    return jsonify({'response' : matches}), 200

@app.route('/mostread', methods=['GET'])
def getMostRead():
    articles = ss.getTopRecentlyRead()
    return jsonify({'response' : articles})

@app.route('/article/rate', methods=['POST'])
def postedArticleRating():
    print 'got request'
    artid = request.form['id']
    resp = request.form['response']
    ss.addVote(artid, resp)
    return jsonify({'response': 'success'}), 200

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
