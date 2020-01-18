# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 11:45:07 2020

@author: abhishekar
"""
import cv2
import json

class FaceRecognitionDataSet:
    empDB=[]
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    def __init__(self):
        self.empDB=[]
        
    #classmethod
    def getObject(cls):
        return cls()
    
    def get_Employe(self, empId):
        user = [ emp for emp in self.empDB if (emp['empId'] == empId) ] 
        return user
    
    def readJson(self, empId):
        with open('users/' + empId + '.json') as json_file:
            data = json.load(json_file)
            print('empId: ' + data['empId'])
            print('name: ' + data['name'])
            #for p in data['users']:
                #print('empId: ' + data['empId'])
                #print('name: ' + data['name'])
                #print('')
            return data
    
    def writeJson(self, user, empId):
        with open('users/' + empId + '.json', 'w') as json_file:
            json.dump(user, json_file, indent=4)
        
    def add_Employe(self, empid, name):
        self.writeJson({"empId": empid, "name": name}, empid)
        count = 0
        cam = cv2.VideoCapture(0)
        cam.set(3, 640) # set video width
        cam.set(4, 480) # set video height
        while(True):
            ret, img = cam.read()
            # img = cv2.flip(img, -1) # flip video image vertically
            print("Abhishek >> FaceRecognitionDataSet")
            print(img)
            print(cv2.COLOR_BGR2GRAY)
            print(cv2)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = self.face_detector.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
                count += 1
                
                # Save the captured image into the datasets folder
                print("image saving start")
                #cv2.imwrite(os.path.join(path , str(face_id) + '_' + str(count) + ".jpg"), img)
                cv2.imwrite("dataset/User." + str(empid) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
                print("image saved")

                cv2.imshow('image', img)

            k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
            if k == 27:
                break
            elif count >= 30: # Take 30 face sample and stop video
                 break

        # Do a bit of cleanup
        print("\n [INFO] Exiting Program and cleanup stuff")
        cam.release()
        cv2.destroyAllWindows()