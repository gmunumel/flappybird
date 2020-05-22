from game.lib import load_image

class BG():
  def __init__(self, screen):
    self.image, self.rect  = load_image('bg.png')
    self.screen = screen

  def draw(self):
    self.screen.blit(self.image, self.rect)