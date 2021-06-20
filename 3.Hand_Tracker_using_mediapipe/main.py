#Importing openCV, mediapipe and time libraries
#importing handtrackingmodule(self-made)
import cv2
import mediapipe as mp
import time
import handtrackingmodule as htm


pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector() #Creating an object from handDetector class

while True:
    #cap.read() returns a boolean(True/False) and if it's true, the frames get stored in the img variable.
    success, img = cap.read()

    #Calling the hand landmark detector functions
    img = detector.findHands(img)

    #Calling the function that will return the coordinates of a particular hand. By default, hand number 0.
    lmList = detector.findPosition(img)

    #to print the coordinates of only one particular landmark(say 4)
    if len(lmList)!=0:
        print(lmList[4])

    #FRAME RATE
    cTime = time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

    #To display the frame rate
    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,255,255),3)

    cv2.imshow("Hand Detector", img)
    #TO TERMINATE THE PROGRAM, PRESS Q
    if cv2.waitKey(1) & 0xFF == ord('q'):
          break
