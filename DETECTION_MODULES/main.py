import cv2
import RPi.GPIO as GPIO
import time
import glob
import face_recognition
import numpy as np
from datetime import datetime
from datetime import date
import mysql.connector
import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Set up the relay module
relay_pin=21,26
GPIO.setup(relay_pin, GPIO.OUT)



FONT=cv2.FONT_HERSHEY_COMPLEX
images=[]
names=[]
today = date.today()
now = datetime.now()
dtString = now.strftime("%H:%M:%P")
path = "/home/sahil/projectend/image/*.*"
for file in glob.glob(path):
    image = cv2.imread(file)
    a=os.path.basename(file)
    b=os.path.splitext(a)[0]
    names.append(b)
    images.append(image)

      

def encoding1(images):
    encode=[]

    for img in images:
        unk_encoding = face_recognition.face_encodings(img)[0]
        encode.append(unk_encoding)
    return encode    

encodelist=encoding1(images)
def mysqladddata(names):
       mydb = mysql.connector.connect(
       host= "localhost",
       user="root",
       password="",
      database="attendance"

)

       a = mydb.cursor()
       sql = ("INSERT IGNORE INTO detected(SNAME,TIMING,RDATE) VALUE(%s,%s,%s)")
       data=(names,dtString,today)

       a.execute(sql,data)
       

       mydb.commit()
       mydb.close()
       
cap =cv2.VideoCapture(0)  
#width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
while True:
      ret,frame=cap.read()
      frame1=cv2.resize(frame,(0,0),None,0.25,0.25)
      face_locations = face_recognition.face_locations(frame1)
      curframe_encoding = face_recognition.face_encodings(frame1,face_locations)
      face_detected = False
      for encodeface,facelocation in zip(curframe_encoding,face_locations):
         face_detected = True
         
         results = face_recognition.compare_faces(encodelist, encodeface)
         distance= face_recognition.face_distance(encodelist, encodeface)
         match_index=np.argmin(distance)
         name=names[match_index]
         mysqladddata(name)
         x1,y1,x2,y2=facelocation
         x1,y1,x2,y2=x1*4,y1*4,x2*4,y2*4
         cv2.rectangle(frame,(y1,x1),(y2,x2),(0,0,255),3)
         cv2.putText(frame,name,(y2+6,x2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),2)
        # Turn on the relay module when a face is detected
         GPIO.output(relay_pin, GPIO.HIGH)
         print("Relay on")
      if not face_detected:
              # Turn off the relay module when no face is detected
            GPIO.output(relay_pin, GPIO.LOW)
            print("Relay off")
        
         
      cv2.imshow("FRAME",frame)
      if cv2.waitKey(1)&0xFF==27:
          break
cap.release()
GPIO.cleanup()
cv2.destroyAllWindows()
