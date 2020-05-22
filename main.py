
from game.bg import BG
from game.globals import *
from pygame.locals import *
import os, pygame, sys, random

pygame.init()

srcSize = (WIN_WIDTH, WIN_HEIGHT)
FPS = 60

screen = pygame.display.set_mode(srcSize)
clock = pygame.time.Clock()
pygame.display.set_caption("Flappy Bird")

def main_game():
  gameOver = False

  bg = BG(screen)

  while not gameOver:

    for event in pygame.event.get():
      if event.type == QUIT:
        gameOver = True
        quit() 

    if pygame.display.get_surface() != None:
      bg.draw()


      pygame.display.update()

    clock.tick(FPS)


def quit():
  pygame.quit()
  sys.exit()

if __name__ == "__main__":
  main_game()