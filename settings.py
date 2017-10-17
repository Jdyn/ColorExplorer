import pygame
import random

# define constant variables
TITLE = "myGame"
WIDTH = 480
HEIGHT = 600
FPS = 60

# define colors
WHITE =  (251, 251, 251)
BLACK = (33, 33, 33)
GREY = (47, 47, 47)
LIGHTGREY = (204, 204, 204)
GREEN = (165, 214, 167)

# Platform List
PLATFORM_LIST = [(0 , HEIGHT - 40, WIDTH, 40),
                 (WIDTH / 2 -10, HEIGHT * 3 / 4, 100, 20),
                 (20, HEIGHT - 300, 85, 20),
                 (420, 200, 50, 20),
                 (WIDTH / 2, HEIGHT * .1, 100, 20)]
# Player properties
PLAYER_ACC = 0.7
PLAYER_FRICTION = -0.10
PLAYER_GRAVITY = 0.7