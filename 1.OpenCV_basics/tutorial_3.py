#drawing shapes/text using OpenCV


#importing OpenCV library
import cv2

#storing video input as a variable
video_capture = cv2.VideoCapture(0)

while True:
    #extracting out the current frame from the video
    success, image = video_capture.read()

    #Drawing a circle
    #cv2.circle(image, centre's coordinates, radius, color, thickness/fill)
    cv2.circle(image, (100,100), 20, (0,0,255), cv2.FILLED)

    #drawing a rectangle
    #cv2.rectangle(image, start_point, end_point, color, thickness/fill)
    cv2.rectangle(image, (150,150), (250,250), (255,0,0), 25)

    #Drawing a line
    #cv2.line(image, start_point, end_point, color, thickness)
    cv2.line(image, (100,100), (150,150),(0,255,0),20)

    #Adding text
    #cv2.putText()
    cv2.putText(image, "Hello", (200,200), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,0),5)

    #displaying the current frame in a window
    cv2.imshow("Title", image)

    #keeping the image open until the next frame
    cv2.waitKey(1)

    #TO TERMINATE THE PROGRAM, PRESS q
    #if cv2.waitKey(1) & 0xFF == ord('q'):
          #break
