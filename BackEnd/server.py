# -*- coding: utf-8 -*-
from flask import Flask, jsonify, abort, request
from flask_cors import CORS, cross_origin

import os
import sys
# sys.path.append('/MKG/BackEnd')
sys.path.append('/Users/baymax/Dev/PyProjects/KG')

from BackEnd import getMethod, postMethod

app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = '/Users/baymax/'


#GET Method
@app.route('/getAllInfo', methods=['GET'])
def get_allInfo():
    res = getMethod.getAllNodeAndRelation()
    return jsonify({'res': res})

@app.route('/getAllNodes', methods=['GET'])
def get_allNodes():
    res = getMethod.getAllNodes()
    return jsonify({'res': res})

@app.route('/getAllRelations', methods=['GET'])
def get_allRelations():
    res = getMethod.getAllRelations()
    return jsonify({'res': res})

@app.route('/getSearchKey', methods=['GET'])
def get_searchKey():
    key = request.values.get('key')
    res = getMethod.getSearchKey(key)
    resp = jsonify({'res': res})
    return resp

#POST METHOD
@app.route('/uploadToCUT', methods=['POST'])
def upload_toCUT():
    senStr = request.json['senStr']
    result = postMethod.handleSentenceCUT(senStr)
    resp = jsonify({'res': result})
    return resp

@app.route('/uploadToNER', methods=['POST'])
def upload_toNER():
    senStr = request.json['senStr']
    result = postMethod.handleSentenceNER(senStr)
    resp = jsonify({'res': result})
    return resp, 200

@app.route('/uploadToRE', methods=['POST'])
def upload_toRE():
    senStr = request.json['senStr']
    result = postMethod.handleSentenceRE(senStr)
    resp = jsonify({'res': result})
    return resp, 200


@app.route('/uploadFile', methods=['POST'])
def uploadOWL():
    # print(request.files['file'])
    file = request.files['file']
    postMethod.uploadFile(file)

    # filename = secure_filename(file.filename)
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    resp = 'ok'
    return resp, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)