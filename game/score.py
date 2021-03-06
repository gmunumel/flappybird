from game.globals import *
import pygame

class Score():
  def __init__(self, screen):
    self.score = 0
    self.font = pygame.font.Font('freesansbold.ttf', 10) 
    self.text = self.font.render('score: {}'.format(self.score), True, WHITE) 
    self.rect = self.text.get_rect()  
    self.rect.right = WIN_WIDTH * 0.90
    self.rect.top = WIN_HEIGHT * 0.05
    self.screen = screen

  def get_score(self):
    return self.score

  def draw(self):
    self.text = self.font.render('score: {}'.format(self.score), True, WHITE) 
    self.screen.blit(self.text, self.rect)

  def update(self):
    self.score += 1