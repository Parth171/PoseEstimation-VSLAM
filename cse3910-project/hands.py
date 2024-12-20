# hands.py
"""
title: Integrating CV2 into a pygame window
author: Laksh Chopra
date-created: 19/3/24
"""

import pygame
from pygame.locals import *
import cv2
import numpy as np
import sys
import mediapipe as mp

"""camera = cv2.VideoCapture(0)
pygame.init()
pygame.display.set_caption("OpenCV in a Pygame Window")
screen = pygame.display.set_mode([1000, 600])
mpDraw = mp.solutions.drawing_utils
mpHands = mp.solutions.hands
hand = mpHands.Hands()

try:
    while True:
        ret, frame = camera.read()
        screen.fill([25, 25, 25])
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hand.process(frame)
        if results.multi_hand_landmarks:

            for hand_landmarks in results.multi_hand_landmarks:
                mpDraw.draw_landmarks(frame, hand_landmarks, mpHands)

            '''for id, lm in enumerate(results.pose_landmarks.landmark):
                h, w, c = frame.shape

                cx, cy = int(lm.x*w), int(lm.y*h)

                cv2.circle(frame, (cx, cy), 10, (0, 255, 0), cv2.FILLED)'''
        frame = np.rot90(frame)
        frame = pygame.surfarray.make_surface(frame)
        screen.blit(frame, (0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
except:
    pygame.quit()
    cv2.destroyAllWindows()"""

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
COLOR = cv2.COLOR_BGR2RGB
if __name__ == "__main__":
    from window import Window
    pygame.init()

    WINDOW = Window("Laksh & Parth Project Menu", 800, 600, 30)

    VIDEO_INPUT = cv2.VideoCapture(0)
    pose = mpPose.Pose()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        ret, POSE_DETECTION_FRAME = VIDEO_INPUT.read()
        POSE_DETECTION_FRAME = cv2.cvtColor(POSE_DETECTION_FRAME, COLOR)
        POSE_ESTIMATION = pose.process(POSE_DETECTION_FRAME)
        if POSE_ESTIMATION.pose_landmarks:
            mpDraw.draw_landmarks(POSE_DETECTION_FRAME, POSE_ESTIMATION.pose_landmarks, mpPose.POSE_CONNECTIONS)

            for id, lm in enumerate(POSE_ESTIMATION.pose_landmarks.landmark):
                HEIGHT, WIDTH, C = POSE_DETECTION_FRAME.shape
                CX, CY = int(lm.x*WIDTH), int(lm.y*HEIGHT)
                cv2.circle(POSE_DETECTION_FRAME, (CX, CY), 10, (0, 255, 0), cv2.FILLED)
        POSE_DETECTION_FRAME = np.rot90(POSE_DETECTION_FRAME)
        POSE_DETECTION_FRAME = pygame.surfarray.make_surface(POSE_DETECTION_FRAME)
        WINDOW.blit(POSE_DETECTION_FRAME, (0, 0))

        WINDOW.updateFrame()

