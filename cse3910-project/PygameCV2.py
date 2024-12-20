# PygameCV2.py
"""
title: Integrating CV2 into a pygame window
author: Laksh Chopra
date-created: 19/3/24
"""

import pygame
import cv2
import numpy as np
import mediapipe as mp

camera = cv2.VideoCapture(0)
pygame.init()
pygame.display.set_caption("OpenCV in a Pygame Window")
screen = pygame.display.set_mode([1000, 600])
mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

try:
    while True:
        ret, frame = camera.read()
        screen.fill([25, 25, 25])
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(frame)
        if results.pose_landmarks:
            mpDraw.draw_landmarks(frame, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
            for id, lm in enumerate(results.pose_landmarks.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                cv2.circle(frame, (cx, cy), 10, (255, 0, 0), cv2.FILLED)
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
    cv2.destroyAllWindows()
