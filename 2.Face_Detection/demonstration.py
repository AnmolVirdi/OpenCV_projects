###Simple program to implement face detection using Haarcascade classifier

import cv2

#A classifier is a ready-made model that is used to detect something(here, face)
# Loading the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam.(A variable form of the video)
cap = cv2.VideoCapture(0)
#Using the realtime video as input

while True:
    #extracting instantenous frame
    check, img = cap.read()

    # Convert to grayscale(Because haar cascade is used for grayscale images only)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    ##################################################################
    # Detecting face using haarcascade classifier.
    # We'll actually get the coordinates covering the facial region as our output.

    #format: face_cascade.detectMultiScale(grayscale image, scale factor, min neighbours)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    #faces will be a tuple storing these values: (topLeft-x,topLeft-y, width, height )



    ##################################################################

    # Drawing a rectangle around each face
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,125,0),2)

    # Displaying the frame
    cv2.imshow('img', img)

    # Stop if q key is pressed
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
