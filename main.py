import pygame as pg
from settings import *
from sprites import *
import random

class Game:
    def __init__(self):
        #initates everything
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("My Game")
        self.clock = pg.time.Clock()
        self.running = True
        
    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()

    def events(self):
        for event in pg.event.get():
        # check for closing the window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
            self.running = False

    def draw(self):
        # Game Loop - draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)

        pg.display.flip()

    def startScreen(self):
         # game start screen
         pass

    def endScreen(self):
        # game over screen
        pass

g = Game()
g.startScreen()
while g.running:
    g.new()
    g.endScreen()

pg.quit()