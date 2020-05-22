from game.lib import load_image

class BG():
  def __init__(self, screen, speed = -5):
    self.image, self.rect  = load_image('bg.png')
    self.image1, self.rect1  = load_image('bg.png')
    self.rect1.left = self.rect.right
    self.speed = speed
    self.screen = screen
    self.movement = [-1 * self.speed, 0]

  def draw(self):
    self.screen.blit(self.image, self.rect)
    self.screen.blit(self.image1, self.rect1)

  def update(self):
    self.rect.left += self.speed
    self.rect1.left += self.speed

    if self.rect.right < 0:
      self.rect.left = self.rect1.right

    if self.rect1.right < 0:
      self.rect1.left = self.rect.right