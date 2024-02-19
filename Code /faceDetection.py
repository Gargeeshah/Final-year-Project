import numpy as np
import cv2

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height

x = input('Enter any key to Record Initial Position')
ret,img = cap.read()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(
    gray,
        
    scaleFactor=1.2,
    minNeighbors=5
    ,     
    minSize=(20, 20)
)

total_stud = len(faces)
print(total_stud)

while True:
    ret, img = cap.read()
    #img = cv2.flip(img, -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        
        scaleFactor=1.2,
        minNeighbors=5
        ,     
        minSize=(20, 20)
    )

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
      

    cv2.imshow('video',img)
    if(len(faces)<total_stud or len(faces)>total_stud):
        print("Suspicious Activity Detected")

    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()
