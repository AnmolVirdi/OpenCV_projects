#To open an image

#importing OpenCV library
import cv2

#Storing the image into a variable using imread() funtion
image = cv2.imread("images/img.jpeg")

#displaying it using imshow() function
cv2.imshow("Title", image)

#To keep the window open
cv2.waitKey(0)
