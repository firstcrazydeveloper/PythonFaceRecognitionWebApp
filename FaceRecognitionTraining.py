# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 12:14:23 2020

@author: abhishekar
"""

import cv2
import numpy as np
from PIL import Image
import os

class FaceRecognitionTraining:
    path = 'dataset'
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    def __init__(self):
        self.path = 'dataset'
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");
        
    # function to get the images and label data
    def getImagesAndLabels(self, path):
    
        imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
        faceSamples=[]
        ids = []
    
        for imagePath in imagePaths:
            PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
            img_numpy = np.array(PIL_img,'uint8')
           
    
            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = self.detector.detectMultiScale(img_numpy)
    
            for (x,y,w,h) in faces:
                faceSamples.append(img_numpy[y:y+h,x:x+w])
                ids.append(id)
    
        return faceSamples,ids
    
    def startTraining(self):
        faces,ids = self.getImagesAndLabels(self.path)
        self.recognizer.train(faces, np.array(ids))
        
        # Save the model into trainer/trainer.yml
        self.recognizer.write('trainer/trainer.yml') # recognizer.save() worked on Mac, but not on Pi
        
        # Print the numer of faces trained and end program
        print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))