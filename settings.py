# game options/settings
TITLE = "ColorExplorer"
WIDTH = 480
HEIGHT = 600
FPS = 60
FONT_NAME = 'arial'
HS_FILE = "highscore.txt"

# Player properties
PLAYER_ACC = 0.7
PLAYER_FRICTION = -0.10
PLAYER_GRAV = 0.7
PLAYER_JUMP = -15

# Starting platforms
PLATFORM_LIST = [(0 , HEIGHT - 40, WIDTH, 40),
                 (WIDTH / 2 -10, HEIGHT * 3 / 4, 100, 20),
                 (20, HEIGHT - 300, 85, 20),
                 (420, 200, 50, 20),
                 (WIDTH / 2, HEIGHT * .1, 100, 20)]

# define colors
WHITE = (251, 251, 251)
BLACK = (47, 47, 47)
GREEN = (165, 214, 167)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
BGCOLOR = BLACK