from game.globals import *
from game.lib import load_image
import pygame

class Bird():
  def __init__(self, screen):
    self.image1, self.rect1 = load_image('bird1.png')
    self.image2, self.rect2 = load_image('bird2.png')
    self.image3, self.rect3 = load_image('bird3.png')
    self.images = [ self.image1, self.image2, self.image3 ]
    self.image = self.images[0]
    self.rect = self.rect1
    self.rect.bottom = WIN_HEIGHT / 2
    self.rect.left = WIN_WIDTH * 0.3
    self.index = 0
    self.counter = 0
    self.gravity = 1.1
    self.jumpVelocity = 11.5
    self.movement = [0, 0]
    self.isDead = False
    self.screen = screen

  def jump(self):
    self.movement[1] = -1 * self.jumpVelocity

  #def get_height(self):
  #  return abs(self.rect.bottom - self.rect.top)

  #def get_width(self):
  #  return abs(self.rect.right - self.rect.left)

  def is_dead(self):
    return self.isDead

  def set_is_dead(self):
    self.isDead = True

  def check_borders(self):
    if self.rect.top < 0 or self.rect.bottom > WIN_HEIGHT:
      self.set_is_dead()

  def draw(self):
    self.screen.blit(self.image, self.rect)

  def update(self):
    if self.counter % 5 == 0:
      self.counter = 0
      self.index = (self.index + 1) % 3
    self.image = self.images[self.index]
    self.counter += 1

    self.movement[1] += self.gravity

    self.rect = self.rect.move(self.movement)
    
