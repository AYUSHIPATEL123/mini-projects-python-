import pyautogui as pag
import cv2 
import numpy as np


# make the video writer
fps=60.0
resolution=(1900,1080)
codec=cv2.VideoWriter_fourcc(*"mp4v")

output=cv2.VideoWriter("miniprojects/video1.mp4",codec,fps,resolution)


# creating window for showing video...
cv2.namedWindow("vediodisplay",cv2.WINDOW_NORMAL)
# cv2.resizeWindow("vidiodisplay",480,280)/qqqqq


# recoring screen

while True:
    img= pag.screenshot()      #take screenshot

    frame = np.array(img)      #convert img to numpy array

    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)  # convert the color to rgb

    output.write(frame)      # write img to video writer

    cv2.imshow('vediodisplay',frame) 

    if cv2.waitKey(1) == ord('q'):        # press q to stop recording
        break

    #display video


output.release()
cv2.destroyAllWindows()