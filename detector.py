import cv2
import numpy as np

faceDetection = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cam = cv2.VideoCapture(0)
rec = cv2.face.LBPHFaceRecognizer_create()
rec.read("recognizer\\trainingData.yml")
id = 0

fontface = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 1.2
fontcolor = (255, 255, 0)

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetection.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        id, conf = rec.predict(gray[y:y + h, x:x + w])
        if id == 1:
            id = "KAUSAR"
        elif id == 2:
            id = "Mrinmoy"
        else:
            id = "Unknown"

        cv2.putText(img, str(id), (x, y + h), fontface, fontscale, fontcolor)
    cv2.imshow("Recognizer", img)
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()