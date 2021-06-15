# Hand Tracker using MediaPipe library

<img src="Extras/demo.gif" alt="drawing" width="200"/>

## About Mediapipe Hands
MediaPipe Hands utilizes an ML pipeline consisting of multiple models working together: A palm detection model that operates on the full image and returns an oriented hand bounding box. A hand landmark model that operates on the cropped image region defined by the palm detector and returns high-fidelity 3D hand keypoints.



## For Beginners
This is a demonstration project for beginners who are new to the game.
- Go through the **HandTrackerDemonstation.py** file first.
- Read the comments! **The steps and dependencies used are elaborated in the code itself**.
- Clone/copy the same project and try fabricating your own variations in the code.

## For the ones who're familiar with the concepts of Classes & Object-oriented programming
- Go through the **handtrackingmodule.py** file
- The **main.py** utilizes this self-created module to demonstrate how we can use this module file in further projects. Instead of building all of it again in the future, we can simply use this module file.

