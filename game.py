import pygame
import src.game_loop
import src.config

class Display():
    def __init__(self):
      pygame.init()
      pygame.display.set_caption("Modular Platformer")
      self.window = pygame.display.set_mode((src.config.WIDTH, src.config.HEIGHT))

class Game():
    def __init__(self):
      self.display = Display() 

      src.game_loop.start(self)


Game()