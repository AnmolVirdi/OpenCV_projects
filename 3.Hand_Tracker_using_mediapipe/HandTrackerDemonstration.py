#Importing openCV, mediapipe and time libraries
import cv2
import mediapipe as mp
import time

#Creating variable to store video using cv2.VideoCapture() function
cap = cv2.VideoCapture(0)

#Assigning the hand detector as well as hand landmarks(points) detector funtions to variables
mpHands= mp.solutions.hands
hands = mpHands.Hands()

#To enable mediapipe's drawing utilities
mpDraw = mp.solutions.drawing_utils

#To generate FRAME RATE (How well is your system coping up with the computations)
pTime = 0 #previous time
cTime = 0 #current time


while True:
    #cap.read() returns a boolean(True/False) and if it's true, the frames get stored in the img variable.
    success, img = cap.read()

    #To make the video frames more readable(to the algorithm), we need to convert it to from BGR to RBG color space.
    img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    #Feeding this more readable img1 to the hands.process function.
    results =  hands.process(img1)

    #print(results.multi_hand_landmarks) uncomment this line to recieve coordinates of all the hand landmarks.

    #okay so if the hand lankmarks are detected,
    if results.multi_hand_landmarks:
        #Going through each landmark because there are 21 landmarks in total. (0-20)
        for handLms in results.multi_hand_landmarks:
            #id is the landmark ID (0-20)
            #lm is the list of coordinates of that landmark
            for id, lm in enumerate(handLms.landmark):



                #To draw those handlandmarks on the video frames
                #The coordinates recieved in lm are actually relative, i.e, 0-1. So, we need to convert them as per the size of original image.

                #Getting height, width and the number of channels of the original images using the .shape function
                height, width, channels = img.shape

                #Converting the relative coordinates(x,y) from lms to original coordinates(cx,cy)
                cx,cy = int(lm.x*width), int(lm.y*height)

                #Now we can draw a circle on each of these landmarks to see them clearly.
                # Format cv2.circle(img, (cx,cy), radius , color , cv2.FILLED)
                cv2.circle(img, (cx,cy), 10 , (255,0,255), cv2.FILLED)

            #To draw landmark lines(Connectors)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)


            #If you want to converge your scope to only one landmark, use conditional statement and then move further.
            #if(id==14):      //14th landmark selected
                #print(id,lm)
                #height, width, channels = img.shape
                #cx,cy = int(lm.x*width), int(lm.y*height)
                #cx,cy = int(lm.x*width), int(lm.y*height)
                #cv2.circle(img, (cx,cy), 10 , (255,0,255), cv2.FILLED)

    #To calculate frames per second
    cTime = time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

    #Displaying Fps on the screen
    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,255,0),3)


    cv2.imshow("Hand Tracker", img)
    cv2.waitKey(1)
