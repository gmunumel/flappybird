
from game.bg import BG
from game.pipe import Pipe
from game.score import Score
from game.globals import *
from pygame.locals import *
import os, pygame, sys, random

pygame.init()

srcSize = (WIN_WIDTH, WIN_HEIGHT)
FPS = 30

screen = pygame.display.set_mode(srcSize)
clock = pygame.time.Clock()
pygame.display.set_caption("Flappy Bird")

def create_pipe(pipes, last_obstacle, gameSpeed):
  if len(pipes) < 3:
    if len(last_obstacle) == 0:
      last_obstacle.add(Pipe(gameSpeed, 1, 1))
      last_obstacle.add(Pipe(gameSpeed, 1, 1, True))
    else:
      for l in last_obstacle:
        if l.rect.right < WIN_WIDTH * 0.75:
          last_obstacle.empty()
          last_obstacle.add(Pipe(gameSpeed, 1, 1))
          last_obstacle.add(Pipe(gameSpeed, 1, 1, True))

def main_game():
  gameOver = False
  gameSpeed = 2

  bg = BG(screen, -1 * gameSpeed)
  score = Score(screen)

  pipes = pygame.sprite.Group()
  last_obstacle = pygame.sprite.Group()

  Pipe.containers = pipes

  while not gameOver:

    for event in pygame.event.get():
      if event.type == QUIT:
        gameOver = True
        quit() 


    # check

    create_pipe(pipes, last_obstacle, gameSpeed)

    bg.update()
    score.update()
    pipes.update()

    if pygame.display.get_surface() != None:
      bg.draw()
      score.draw()
      pipes.draw(screen)


      pygame.display.update()

    clock.tick(FPS)


def quit():
  pygame.quit()
  sys.exit()

if __name__ == "__main__":
  main_game()