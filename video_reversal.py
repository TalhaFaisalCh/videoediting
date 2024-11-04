#!/usr/bin/env python3
import cv2
import numpy as np
import os

file_name = input('Name your video: ')+'.mp4'

# strictly say 'y'(doesn't matter if its capital or not) if you want to video reverse 
choice = input("reverse the video?[Y/N]: ").upper()

# Open the default camera
cam = cv2.VideoCapture(0)
# To get grayscale, change the variable coloredvideo to False below
coloredvideo = True
# Get the default frame width and height (CAP = capture)(PROP = property)
frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
# If you want to enable change size, replace frame_width and frame_height with the program infront of it and enable it by removing '#'
new_width = frame_width #int(input('Width: '))
new_height = frame_height #int(input('Height: '))
# Define the codec and create VideoWriter object (fourcc == Four character code) 
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# If you want to specify a path, add to filename variable e.g D:\folder\filename.mp4
out = cv2.VideoWriter(file_name,  
                      fourcc, 30.0, (new_width, new_height), isColor=coloredvideo)

print(new_width, new_height)

list_frame = []
while True:
    ret, frame = cam.read()
    if ret == False:
        print("Camera reading failed, know why?")
        quit()
    resized_image = cv2.resize(frame, (new_width, new_height))
    # If you want to have grayscale video, look above
    if coloredvideo == False:
        resized_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    list_frame.append(resized_image)

    # Display the captured frame
    cv2.imshow(file_name, resized_image)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) == ord('q'):
        break

# nFrames = number frames
nFrames = len(list_frame)
start = 10
# Cuts out the part where camera shuts down, it is obvious if you remove '-10'
end = nFrames - 10
step = 1
# (if the input choice is 'Y', then is true, so (choice == 'Y') = True. Else it will be false)
reverse = (choice == 'Y')
if reverse:
    start = nFrames - 10
    end = 10
    step = -1
for i in range(start, end, step):
    out.write(list_frame[i])

# If you want to have a specific path, go to line 25 and disable the print statement below with '#' at beginning
print('Video saved at',os.getcwd() + '\\' + file_name)

# Release the capture and writer objects
cam.release()
out.release()
cv2.destroyAllWindows()
