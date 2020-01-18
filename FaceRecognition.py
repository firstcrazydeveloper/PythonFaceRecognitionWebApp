# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 12:20:44 2020

@author: abhishekar
"""

import cv2
import numpy as np
import FaceRecognitionDataSet



class FaceRecognition:
    faceRecognitionDataSet = FaceRecognitionDataSet.FaceRecognitionDataSet()
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);
    font = cv2.FONT_HERSHEY_SIMPLEX
    id = 0
    def __init__(self):
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read('trainer/trainer.yml')
        self.cascadePath = "haarcascade_frontalface_default.xml"
        self.faceCascade = cv2.CascadeClassifier(self.cascadePath);
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.id = 0
        
    def startRecognition(self):
        # Initialize and start realtime video capture
        cam = cv2.VideoCapture(0)
        cam.set(3, 640) # set video widht
        cam.set(4, 480) # set video height
        
        # Define min window size to be recognized as a face
        minW = 0.1*cam.get(3)
        minH = 0.1*cam.get(4)
        while(True):
            ret, img = cam.read()
            #img = cv2.flip(img, -1) # Flip vertically            
        
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        
            faces = self.faceCascade.detectMultiScale( 
                gray,
                scaleFactor = 1.2,
                minNeighbors = 5,
                minSize = (int(minW), int(minH)),
               )
        
            for(x,y,w,h) in faces:
        
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        
                id, confidence = self.recognizer.predict(gray[y:y+h,x:x+w])
        
                # Check if confidence is less them 100 ==> "0" is perfect match 
                if (confidence < 100):
                    user = self.faceRecognitionDataSet.readJson(str(id))
                    print("User >> Start Recognition")
                    print(user)
                    id = user['name']
                    confidence = "  {0}%".format(round(100 - confidence))
                else:
                    id = "unknown"
                    confidence = "  {0}%".format(round(100 - confidence))
                
                cv2.putText(img, str(id), (x+5,y-5), self.font, 1, (255,255,255), 2)
                cv2.putText(img, str(confidence), (x+5,y+h-5), self.font, 1, (255,255,0), 1)  
            
            cv2.imshow('camera',img) 
        
            k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
            if k == 27:
                break
    
        # Do a bit of cleanup
        print("\n [INFO] Exiting Program and cleanup stuff")
        cam.release()
        cv2.destroyAllWindows()