from flask import Flask, jsonify
from flask import abort, make_response, request
from flask.ext.httpauth import HTTPBasicAuth
from flask_cors import CORS, cross_origin
auth = HTTPBasicAuth()
from app import app
from storageservice import StorageService
import config
from analysisengine import AnalysisEngine

CORS(app)

ss = StorageService(config.dbAddr)
ae = AnalysisEngine(ss)

@app.route('/test', methods=['GET'])
def test():
    #resp = ss.es.get(index='sw', doc_type='people', id=1)
    return jsonify(resp)

@app.route('/process', methods=['POST'])
@auth.login_required
def processDocument():
    ae.inputDocument(request)
    #inject document into the sentiment module
    return jsonify({'msg':'success'}), 201

@app.route('/summarize', methods=['POST'])
def summarizeUserDocument():
    result = ae.returnDocument(request)
    return jsonify({'response' : result})

@auth.get_password
def get_password(username):
    if username == 'jake':
        return 'python'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
