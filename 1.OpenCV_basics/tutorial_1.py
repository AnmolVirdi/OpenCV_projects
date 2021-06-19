#To open the camera using OpenCV

#importing OpenCV library
import cv2

#storing video input as a variable
video_capture = cv2.VideoCapture(0)

while True:
    #extracting out the current frame from the video
    success, image = video_capture.read()

    #displaying the current frame in a window
    cv2.imshow("Title", image)

    #keeping the image open until the next frame
    cv2.waitKey(1)

    #TO TERMINATE THE PROGRAM, PRESS q
    #if cv2.waitKey(1) & 0xFF == ord('q'):
          #break
