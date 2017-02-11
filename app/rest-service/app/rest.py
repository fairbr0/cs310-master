from flask import Flask, jsonify
from flask import abort, make_response, request
from flask.ext.httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()
from app import app
import config
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q
import logging
logging.basicConfig(level=logging.DEBUG)

es = Elasticsearch([{'host':config.host, 'port':config.port}])
outlets = ['BBC', 'The Guardian', 'CNN', 'Home']

@app.route('/alive', methods=['GET'])
def alive():
    return jsonify({'msg':'success'}), 200

#returns a list of news outlets
@app.route('/outlets', methods=['GET'])
def getOutlets():
    return jsonify({'outlets':outlets}), 200

#return a list of articles from the selected news outlets
@app.route('/outlet/<outlet>', methods=['GET'])
@app.route('/outlet/<outlet>/<id>', methods=['GET'])
def getOutletArticles(outlet, id=None):
    logging.debug(outlet)
    if id is not None:
        logging.debug(id)
    else:

    return jsonify({'msg':'success'}), 200

#return a list of top keywords
@app.route('/keywords', methods=['GET'])
def getKeywords():
    return jsonify({'msg':'success'}), 200

#returns a list of articles with selected keyword
@app.route('/keywords/<keyword>', methods=['GET'])
@app.route('/keywords/<keyword>/<id>', methods=['GET'])
def getKeywordArticles(keyword, id=None):
    logging.debug(keyword)
    if id is not None:
        logging.debug(id)
    return jsonify({'msg':'success'}), 200


#returns a list of most recent
@app.route('/gettop', methods=['GET'])
@app.route('/gettop/<id>', methods=['GET'])
def getTopArticlesNext(id=None):
    if id is not None:
        logging.debug(id)
    return jsonify({'msg':'success'}), 200

#returns list of most recent from chosen outlets
@app.route('/gettopoutlets/<outlets>', methods=['GET'])
@app.route('/gettopoutlets/<outlets>/<id>', methods=['GET'])
def getTopArticlesOutlets(outlets, id=None):
    logging.debug(outlets)
    if id is not None:
        logging.debug(id)
    return jsonify({'msg':'success'}), 200


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
