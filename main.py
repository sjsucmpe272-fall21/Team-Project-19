import cv2
import numpy as np
import face_recognition
import os, time
from attendance import mark_attendance
from email_attach import send_email
import pandas as pd


path = 'Training_images'
to_email = "haard.dravid@gmail.com"
df = pd.DataFrame(columns=["Name","TimeStamp"])
df.to_excel("temp.xlsx", index=False)
images = []
classNames = []
myList = os.listdir(path)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])


def findEncodings(images):
    encodeList = []


    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


encodeListKnown = findEncodings(images)
print('Encoding Complete')

cap = cv2.VideoCapture(0)
timeout = time.time() + 30
while time.time()<=timeout:
    success, img = cap.read()

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            name = name.split("_")[0]
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            if mark_attendance(name):
                cv2.putText(img, "Attendance Recorded", (x1 - 2, y2 + 25), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            else:
                cv2.putText(img, "Already recorded", (x1 - 2, y2 + 25), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
    
    cv2.imshow('Webcam', img)
    key = cv2.waitKey(1)        

send_email(to_email, "temp.xlsx")