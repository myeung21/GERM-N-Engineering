# facial_tracking.py
''' This code enables Simon to identify faces using a rasp pi 4
    camera and calculates where to move when a user moves within
    the camera's vision using a standard motor '''

import numpy as np
import cv2
import serial
import RPi.GPIO as GPIO
import time
import threading

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

chan_list = [11,13]
flag = True

GPIO.setup(chan_list, GPIO.OUT)

x = 200
y = 200
#status = 0

maxy = 0
maxx = 0

face_cascade = cv2.CascadeClassifier('/home/pi/Desktop/faces.xml')
eye_cascade = cv2.CascadeClassifier('/home/pi/Desktop/faces.xml')

cap = cv2.VideoCapture(0)

def blink(pin):
    GPIO.output(pin,GPIO.HIGH)  
    time.sleep(1)  
    GPIO.output(pin,GPIO.LOW)  
    time.sleep(1)
    return
        
def xyblink():

    while True:
        if x > 200 and y > 200:
            blink(chan_list)
        else:
            time.sleep(1)
            print('hi')
            
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord("q"):
            break
            
def facialtrack():
    global x
    global y
    while 1:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            
            x = x + (w/2)
            y = y + (h/2)
            visionx3()
            visiony2()
             
            #asks if a face has been detected
            
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                
        cv2.imshow('img',img)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"): #quit command
            break
            
def visiony2():
    y_d = float(200)
    e_y = y - y_d
    maxDC_Change_y = (7.0 - 5.5) / 2 #the max change from middle of "y"
    percentY_Change = e_y / y_d
    newDutyCycle_y = (maxDC_Change_y * percentY_Change) + 6.25
    ymot.ChangeDutyCycle(newDutyCycle_y)

def visionx3():
    global newDutyCycle_x
    inrange = array[int(round(x))]
    newDutyCycle_x = newDutyCycle_x + 0.1 * inrange
    newDutyCycle_x = ( float(array2[int(round(newDutyCycle_x*10))]) ) / 10
    xmot.ChangeDutyCycle(newDutyCycle_x)
    
global array    
array = []
for x in range(200):
    array.append(1)
for x in range(200):
    array.append(0)
for x in range(300):
    array.append(-1)
    
global array2
b = list(range(50,106))
a = []
c = []
for x in range(50):
    a.append(50)
for x in range(51):
    c.append(100)
array2 = np.concatenate([a,b,c])

global newDutyCycle_x
newDutyCycle_x = float(7.5)
newDutyCycle_y = float(6.25)
ymot = GPIO.PWM(11, 50)
xmot = GPIO.PWM(13, 50)
ymot.start(6.25)
xmot.start(7.5)
facialtrack()
            

cap.release()
cv2.destroyAllWindows()
print("I am not dead")

GPIO.cleanup()
