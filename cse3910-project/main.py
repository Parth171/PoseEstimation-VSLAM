# main.py
"""
Title: The main program file
date-created: 05/06/2024
authors: Parth Sakpal & Laksh Chopra
"""

import pygame
#from Window import Window
import cv2
import numpy as np
import mediapipe as mp
from window import Window
from button import Button


### VARIABLES ###
CAMERA_FEED = cv2.VideoCapture(0)
MP_DRAW = mp.solutions.drawing_utils
MP_POSE = mp.solutions.pose
POSE = MP_POSE.Pose()
WINDOW = Window("Pose Estimation Simulator")

THERMAL = Button(100, 60)
THERMAL.setPOS(WINDOW.getWidth()-THERMAL.getSurface().get_width()-28, 100)
THERMAL.setColor((242, 69, 46))

SATURATION = Button(100, 60)
SATURATION.setPOS(WINDOW.getWidth()-SATURATION.getSurface().get_width()-28, 210)
SATURATION.setColor((255, 234, 115))

RESET = Button(100, 60)
RESET.setPOS(WINDOW.getWidth()-RESET.getSurface().get_width()-28, 320)

thermal_true = False
saturation_true = False
reset_true = False




if __name__ == "__main__":
    pygame.init()
    pygame.font.init()

    FONT = pygame.font.SysFont('Corbel', 20)
    thermal_text = FONT.render('Thermal ', True, (255, 255, 255))
    saturation_text = FONT.render('Saturation ', True, (255, 255, 255))
    reset_text = FONT.render('Cool ', True, (255, 255, 255))

    THERMAL.setColor((242, 69, 46))
    SATURATION.setColor((255, 234, 115))


    while True:

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if THERMAL.getX() <= mouse[0] <= THERMAL.getX() + 100 and THERMAL.getY() <= mouse[1] <= THERMAL.getY() + 60:


                    thermal_true = True
                    saturation_true = False
                    reset_true = False

                if SATURATION.getX() <= mouse[0] <= SATURATION.getX() + 100 and SATURATION.getY() <= mouse[1] <= SATURATION.getY() + 60:



                    saturation_true = True
                    thermal_true = False
                    reset_true = False

                if RESET.getX() <= mouse[0] <= RESET.getX() + 100 and RESET.getY() <= mouse[1] <= RESET.getY() + 60:



                    saturation_true = False
                    thermal_true = False
                    reset_true = True

        FRAME_AVAILABLE, FRAME = CAMERA_FEED.read()
        FRAME = cv2.cvtColor(FRAME, cv2.COLOR_BGR2RGB)

        if saturation_true is True:
            FRAME = cv2.cvtColor(FRAME, cv2.COLOR_BGR2Lab)

        if thermal_true is True:
            FRAME = cv2.cvtColor(FRAME, cv2.COLOR_BGR2HSV)

        if reset_true is True:
            FRAME = cv2.cvtColor(FRAME, cv2.COLOR_BGR2RGB)






        RESULTS = POSE.process(FRAME)
        if RESULTS.pose_landmarks:
            MP_DRAW.draw_landmarks(FRAME, RESULTS.pose_landmarks, MP_POSE.POSE_CONNECTIONS)
            for id, lm in enumerate(RESULTS.pose_landmarks.landmark):
                HEIGHT, WIDTH, KEY_POINT = FRAME.shape

                KEYPOINT_X, KEYPOINT_Y = int(lm.x*WIDTH), int(lm.y*HEIGHT)
                cv2.circle(FRAME, (KEYPOINT_X, KEYPOINT_Y), 10, (255, 0, 0), cv2.FILLED)

            FRAME = np.rot90(FRAME)
            FRAME = pygame.surfarray.make_surface(FRAME)

            WINDOW.getSurface().blit(FRAME, (0, 50))
            WINDOW.getSurface().blit(THERMAL.getSurface(), THERMAL.getPOS())
            WINDOW.getSurface().blit(thermal_text, (THERMAL.getX(), THERMAL.getY() - 15))
            WINDOW.getSurface().blit(saturation_text, (SATURATION.getX(), SATURATION.getY() - 15))
            WINDOW.getSurface().blit(reset_text, (RESET.getX(), RESET.getY() - 15))
            WINDOW.getSurface().blit(SATURATION.getSurface(), SATURATION.getPOS())
            WINDOW.getSurface().blit(RESET.getSurface(), RESET.getPOS())




            WINDOW.updateFrame()


