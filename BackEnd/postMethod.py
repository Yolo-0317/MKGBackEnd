# -*- coding: utf-8 -*-
from flask import Flask, jsonify, abort, request
import requests, os

from BackEnd.NLP import NER, RE_Sentence, CUT

UPLOAD_FOLDER = '/Users/baymax'

# 接收上传文件
def uploadFile(file):
    # file = request.files['file']
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))

#CUT
def handleSentenceCUT(senStr):
    return CUT.cutSenStr(senStr)

#NER
def handleSentenceNER(senStr):
    return NER.handleSentence(senStr)

#RE
def handleSentenceRE(senStr):
    return  RE_Sentence.sentence_re(senStr)