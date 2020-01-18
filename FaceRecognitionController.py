# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 11:41:13 2020

@author: abhishekar
"""
import FaceRecognitionDataSet
import FaceRecognitionTraining
import FaceRecognition
from flask import Flask
from flask import jsonify
from flask import request
from os import environ
app = Flask(__name__)

faceRecognitionDataSet = FaceRecognitionDataSet.FaceRecognitionDataSet()
faceRecognitionTraining = FaceRecognitionTraining.FaceRecognitionTraining()
faceRecognition = FaceRecognition.FaceRecognition()
@app.route('/facerecognition/user',methods=['POST'])
def createUser():
    dat = {
    'empId':request.json['empId'],
    'name':request.json['name']
    }
    faceRecognitionDataSet.add_Employe(request.json['empId'], request.json['name'])
    faceRecognitionTraining.startTraining()
    return jsonify(dat)
@app.route('/facerecognition/start',methods=['get'])
def startRecognition():
    print("Start Recognition")
    faceRecognition.startRecognition()
    return jsonify({'response':'Success'})


if __name__ == '__main__':
    #HOST = environ.get('SERVER_HOST', 'localhost')
    #try:
        #PORT = int(environ.get('SERVER_PORT', '5555'))
    #except ValueError:
        #PORT = 5555
    #app.run(HOST, PORT)
    app.run(host = '0.0.0.0', port = 4200)