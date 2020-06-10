from game.globals import *
from game.lib import load_image
import pygame

class Pipe(pygame.sprite.Sprite):
  def __init__(self, speed = 5, rand = 0.3, vFlip = False):
    pygame.sprite.Sprite.__init__(self, self.containers)
    self.image, self.rect = load_image('pipe.png')

    if (vFlip):
      self.image = pygame.transform.flip(self.image, False, True)
      self.rect.bottom = int(abs(rand - 0.2) * WIN_HEIGHT)  
    else:
      self.rect.top = int(rand * WIN_HEIGHT)  

    self.rect.left = WIN_WIDTH + self.rect.width

    self.movement = [-1 * speed, 0]

  def draw(self):
    screen.blit(self.image, self.rect)

  def update(self):
    self.rect = self.rect.move(self.movement)

    if self.rect.right < 0:
      self.kill()