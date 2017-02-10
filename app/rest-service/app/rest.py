from flask import Flask, jsonify
from flask import abort, make_response, request
from flask.ext.httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()
from app import app
import config
from elasticService import ElasticService

es = ElasticService(config.elasticAddr)

@app.route('/test', methods=['GET'])
def test():

    resp = es.es.get(index='sw', doc_type='people', id=1)
    return jsonify(resp)


'''@app.route('/summary/getDocuments', methods=['GET'])
def get_tasks():
    #get the documents
    document = document_loader()
    resp = {"id":document.id, "title":document.title, "content":document.body, "author":document.author, "date":document.date, "source":document.url, "url":document.url}
    return jsonify(resp)

@auth.get_password
def get_password(username):
    if username == 'jake':
        return 'python'
    return None
'''
@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)