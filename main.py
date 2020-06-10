from game.bg import BG
from game.pipe import Pipe
from game.score import Score
from game.bird import Bird
from game.globals import *
from pygame.locals import *
import os, pygame, sys, random

pygame.init()

srcSize = (WIN_WIDTH, WIN_HEIGHT)
FPS = 30

screen = pygame.display.set_mode(srcSize)
clock = pygame.time.Clock()
pygame.display.set_caption("Flappy Bird")


def check_collide(bird, pipes):
  for pipe in pipes:
    if pygame.sprite.collide_mask(bird, pipe):
      bird.set_is_dead()

  bird.check_borders()

def create_pipe(pipes, last_obstacle, gameSpeed):
  if len(last_obstacle) == 0:
    rand = random.randrange(40, 80) / 100
    last_obstacle.add(Pipe(gameSpeed, rand))
    last_obstacle.add(Pipe(gameSpeed, rand, True))
  else:
    for l in last_obstacle:
      if l.rect.right < WIN_WIDTH * 0.65:
        last_obstacle.empty()
        rand = random.randrange(40, 80) / 100
        last_obstacle.add(Pipe(gameSpeed, rand))
        last_obstacle.add(Pipe(gameSpeed, rand, True))
        break

def main_game():
  gameOver = False
  gameSpeed = 2

  bg = BG(screen, -1 * gameSpeed)
  score = Score(screen)
  bird = Bird(screen)

  pipes = pygame.sprite.Group()
  last_obstacle = pygame.sprite.Group()

  Pipe.containers = pipes

  while not gameOver:

    for event in pygame.event.get():
      if event.type == QUIT:
        gameOver = True
        quit() 

      if event.type == KEYDOWN:
        if event.key == K_SPACE or event.key == K_UP:
          bird.jump()

    check_collide(bird, pipes)

    create_pipe(pipes, last_obstacle, gameSpeed)

    bg.update()
    score.update()
    pipes.update()
    bird.update()

    if pygame.display.get_surface() != None:
      bg.draw()
      score.draw()
      pipes.draw(screen)
      bird.draw()

      pygame.display.update()

    if bird.is_dead():
      gameOver = True

    clock.tick(FPS)


def quit():
  pygame.quit()
  sys.exit()

if __name__ == "__main__":
  main_game()