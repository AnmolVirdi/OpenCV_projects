#Importing openCV, mediapipe and time libraries
import cv2
import mediapipe as mp
import time


#Creating a Class/prototype
class handDetector():

    #Constructor, with some default values
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon=trackCon

        #Assigning the hand detector as well as hand landmarks(points) detector funtions to variables of the class
        self.mpHands= mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,self.detectionCon,self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils


    #function to detect hands and place/draw landmarks on them
    def findHands(self, img, draw=True):
        img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results =  self.hands.process(img1)
        #print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

        return img

    #Function to find coordinates of all the landmarks of a particular hand(default= hand number 0). Returns a list of all of them.
    def findPosition(self, img, handNo=0, draw=True):

        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                #if(id==14):
                    #print(id,lm)
                height, width, channels = img.shape
                cx,cy = int(lm.x*width), int(lm.y*height)
                #print(id, cx, cy)
                lmList.append([id, cx,cy])
                if draw:
                    cv2.circle(img, (cx,cy), 10, (255,0,0), cv2.FILLED)

        return lmList


#Implementation/Check
def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if len(lmList)!=0:
            print(lmList[4])
        #FRAME RATE
        cTime = time.time()
        fps=1/(cTime-pTime)
        pTime=cTime

        cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,255,0),3)

        cv2.imshow("Hello", img)
        cv2.waitKey(1)

if __name__=="__main__":
    main()
