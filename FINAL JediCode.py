#Final
from collections import deque
import numpy as np
import imutils
import cv2
import urllib
import BOT
from math import pi
# import turtle
#turtle.showturtle()

cap = cv2.VideoCapture(0)

lower_orange = np.array([0,112,94])
upper_orange = np.array([28,255,255])

#x limits for centre so that the bot is in line with the ball
xLowerLimit = 0
xUpperLimit = 0

while True:

    key = cv2.waitKey(1) & 0xFF
    if(key == ord("q")):
                break


    ret, frame = cap.read()

    if(ret == False):
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_orange, upper_orange)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    xLowerLimit = frame.shape[0]/2 - 50
    xUpperLimit = frame.shape[0]/2 + 50

    #if len(cnts)==0, keep rotating the bot bit by bit until the circle is found and is in the middle of the screen
    #if len(cnts) > 0, rotate more so the ball is somewhere in the middle of the screen

    if len(cnts) > 0:
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

            if radius > 10:
                        cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
            a=int(x)
            b=int(y)
            r=int(radius)
# print(a,b,r)

            #if a is not in some range (somewhere in the middle of the screen depending
            #on how the camera is kept and how the ball catcher is attached)
            #then rotate the bot a bit more and use "continue"

            if(not a > xLowerLimit and a < xUpperLimit):
                BOT.turn_clockwise(10*pi/180)
                continue
            #move bit by bit if radius > 10 and <130

            #if(r>10 and r<130):
            #    turtle.forward(2)

            if(r>10 and r<130):
                BOT.move_forward(5)

    else:
        #rotate the bot by a bit around 10 degrees or 15 degrees
        BOT.turn_clockwise(12.5*pi/180)
 pass
   # cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()



