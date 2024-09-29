#!/usr/bin/env python3
import cv2
import numpy as np

choice = input("reverse the video?[Y/N]: ").upper()

# Open the default camera
#cam = cv2.VideoCapture('/Users/faisalshafait/Documents/PythonCode/output.mp4')
cam = cv2.VideoCapture(0)

# Get the default frame width and height
frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
new_width = int(input('Width >>>'))
new_height = int(input('Height >>>'))
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('/Users/faisalshafait/Documents/PythonCode/NEWoutput.mp4', 
                      fourcc, 30.0, (new_width, new_height), isColor=False)
print(frame_height, frame_width)
list_frame = []
while True:
    ret, frame = cam.read()
    resized_image = cv2.resize(frame, (new_width, new_height))
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    list_frame.append(gray_image)

    # Display the captured frame
    cv2.imshow('Talha\'s livestream', gray_image)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) == ord('q'):
        break

nFrames = len(list_frame)
start = 10
end = nFrames - 10
step = 1
reverse = (choice == 'Y')
if reverse:
    start = nFrames - 10
    end = 10
    step = -1
for i in range(start, end, step):
    out.write(list_frame[i])


# Release the capture and writer objects
cam.release()
out.release()
cv2.destroyAllWindows()
