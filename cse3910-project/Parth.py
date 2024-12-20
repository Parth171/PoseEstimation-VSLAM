"""'''
Title: Parth's Classes
Date-created: 3/8/2024
Author: Parth Sakpal
'''

import cv2
import mediapipe as mp
import time
# cv2 is used for image processing, and mediapipe is used for pose estimation

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose

pose = mpPose.Pose() # Come back to this function later


vid = cv2.VideoCapture(0)

Ptime = 0

while True:

    _, frame = vid.read()



    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    GRAY = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lab = cv2.cvtColor(frame, cv2.COLOR_BGR2Lab)

    #COLOR_BGR2RGB

    results = pose.process(frame)

    if results.pose_landmarks:
        mpDraw.draw_landmarks(frame, results.pose_landmarks, mpPose.POSE_CONNECTIONS)

        for id, lm in enumerate(results.pose_landmarks.landmark):

            h, w, c = frame.shape
            #print(id, lm)

            cx, cy = int(lm.x * w), int(lm.y * h)

            cv2.circle(frame, (cx,cy), 10, (255,0,0), cv2.FILLED)


    cv2.imshow("Camera", frame)



    if cv2.waitKey(5) == ord("e"):
        break

cv2.destroyAllWindows()

"""


import pygame
import sys

# initializing the constructor
pygame.init()

# screen resolution
res = (720, 720)

# opens up a window
screen = pygame.display.set_mode(res)

# white color
color = (255, 255, 255)

# light shade of the button
color_light = (170, 170, 170)

# dark shade of the button
color_dark = (100, 100, 100)

# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
height = screen.get_height()

# defining a font
smallfont = pygame.font.SysFont('Corbel', 35)

# rendering a text written in
# this font
text = smallfont.render('quit', True, color)

while True:

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

        # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:

            # if the mouse is clicked on the
            # button the game is terminated
            if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                pygame.quit()

            # fills the screen with a color
    screen.fill((60, 25, 60))

    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()

    # if mouse is hovered on a button it
    # changes to lighter shade
    if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
        pygame.draw.rect(screen, color_light, [width / 2, height / 2, 140, 40])

    else:
        pygame.draw.rect(screen, color_dark, [width / 2, height / 2, 140, 40])

    # superimposing the text onto our button
    screen.blit(text, (width / 2 + 50, height / 2))

    # updates the frames of the game
    pygame.display.update()





""""""
"""


import pygame
#from Window import Window
import cv2
import numpy as np
import mediapipe as mp

### VARIABLES ###
CAMERA_FEED = cv2.VideoCapture(0)
MP_DRAW = mp.solutions.drawing_utils
MP_POSE = mp.solutions.pose
POSE = MP_POSE.Pose()


if __name__ == "__main__":
    from window import Window
    from button import Button
    pygame.init()

    WINDOW = Window("Pose Estimation Simulator")
    BUTTON = Button(200,100)

    BUTTON.setPOS(100,100)

    thermal = False




    while True:

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if BUTTON.getX()  <= mouse[0] <= BUTTON.getX() + 200 and BUTTON.getY() <= mouse[1] <= BUTTON.getY() + 100:
                    thermal = True

        FRAME_AVAILABLE, FRAME = CAMERA_FEED.read()
        FRAME = cv2.cvtColor(FRAME, cv2.COLOR_BGR2RGB)
        if thermal is True:
            FRAME = cv2.cvtColor(FRAME, cv2.COLOR_BGR2Lab)
        RESULTS = POSE.process(FRAME)
        if RESULTS.pose_landmarks:
            MP_DRAW.draw_landmarks(FRAME, RESULTS.pose_landmarks, MP_POSE.POSE_CONNECTIONS)
            for id, lm in enumerate(RESULTS.pose_landmarks.landmark):
                HEIGHT, WIDTH, KEY_POINT = FRAME.shape

                KEYPOINT_X, KEYPOINT_Y = int(lm.x*WIDTH), int(lm.y*HEIGHT)
                cv2.circle(FRAME, (KEYPOINT_X, KEYPOINT_Y), 10, (255, 0, 0), cv2.FILLED)

            FRAME = np.rot90(FRAME)
            FRAME = pygame.surfarray.make_surface(FRAME)

            WINDOW.getSurface().blit(FRAME, (0, 0))
            WINDOW.getSurface().blit(BUTTON.getSurface(), BUTTON.getPOS())
            WINDOW.updateFrame()



"""