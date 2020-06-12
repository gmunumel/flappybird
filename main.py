from game.bg import BG
from game.ground import Ground
from game.pipe import Pipe
from game.score import Score
from game.bird import Bird
from game.globals import *
from pygame.locals import *
import os, pygame, sys, random, neat

DRAW_LINES = True

pygame.init()

srcSize = (WIN_WIDTH, WIN_HEIGHT)
FPS = 30

screen = pygame.display.set_mode(srcSize)
clock = pygame.time.Clock()
pygame.display.set_caption("Flappy Bird")

def check_collide(birds, pipes, genomes_track, nets):
  for pipe in pipes:
    for i, bird in enumerate(birds):
      if pygame.sprite.collide_mask(bird, pipe):
        bird.set_is_dead()
        genomes_track[i].fitness -= 1
        birds.pop(i)
        nets.pop(i)
        genomes_track.pop(i)
      else:
        bird.check_borders()
        if (bird.is_dead()):
          genomes_track[i].fitness -= 1
          birds.pop(i)
          nets.pop(i)
          genomes_track.pop(i)

def create_pipe(pipes_s, last_obstacle, gameSpeed):
  if len(last_obstacle) == 0:
    new_pipe = Pipe(gameSpeed, 0.6)
    pipes_s.append(new_pipe)
    last_obstacle.add(new_pipe)
    new_pipe = Pipe(gameSpeed, 0.6, True)
    pipes_s.append(new_pipe)
    last_obstacle.add(new_pipe)
  else:
    for l in last_obstacle:
      if l.rect.right < WIN_WIDTH * 0.4:
        last_obstacle.empty()
        rand = random.randrange(35, 60) / 100
        new_pipe = Pipe(gameSpeed, rand)
        pipes_s.append(new_pipe)
        last_obstacle.add(new_pipe)
        new_pipe = Pipe(gameSpeed, rand, True)
        pipes_s.append(new_pipe)
        last_obstacle.add(new_pipe)
        break

def update_fitness(birds, pipes_s, genomes_track, nets):
  for genome_track in genomes_track:
    genome_track.fitness += 5

  for i, bird in enumerate(birds):
    genomes_track[i].fitness += 0.1

    distance = nets[i].activate((bird.rect.top, abs(bird.rect.top - pipes_s[0].rect.top), 
                                abs(bird.rect.top - pipes_s[1].rect.bottom)))

    if distance[0] > 0.5:
      bird.jump()

def main_game(genomes, config):
  gameSpeed = 2
  gameOver = False

  nets = []
  genomes_track = []
  birds = []
  pipes_s = []

  for _, genome in genomes:
    net = neat.nn.FeedForwardNetwork.create(genome, config)
    nets.append(net)
    birds.append(Bird(screen))
    genome.fitness = 0
    genomes_track.append(genome)

  bg = BG(screen, -1 * gameSpeed)
  ground = Ground(screen, -1 * gameSpeed)
  score = Score(screen)

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
          for bird in birds:
            bird.jump()

    check_collide(birds, pipes, genomes_track, nets)

    create_pipe(pipes_s, last_obstacle, gameSpeed)

    for bird in birds:
      bird.update()
    
    update_fitness(birds, pipes_s, genomes_track, nets)

    bg.update()
    pipes.update()
    ground.update()
    score.update()

    if len(pipes) < len(pipes_s):
      pipes_s.pop(0)
      pipes_s.pop(0)

    if pygame.display.get_surface() != None:
      bg.draw()
      pipes.draw(screen)
      ground.draw()
      score.draw()
      
      for bird in birds:
        bird.draw()

        if DRAW_LINES:
          pygame.draw.line(screen, (255,0,0), 
            (bird.rect.left + bird.image.get_width()/2, bird.rect.top + bird.image.get_height()/2), 
            (pipes_s[0].rect.left + pipes_s[0].image.get_width()/2, pipes_s[0].rect.top), 5)
          pygame.draw.line(screen, (255,0,0), 
            (bird.rect.left + bird.image.get_width()/2, bird.rect.top + bird.image.get_height()/2), 
            (pipes_s[0].rect.left + pipes_s[1].image.get_width()/2, pipes_s[1].rect.bottom), 5)

      pygame.display.update()

    if len(birds) == 0:
      gameOver = True

    clock.tick(FPS)


def run_neat(config_path):
  config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, 
    neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

  population = neat.Population(config)

  population.add_reporter(neat.StdOutReporter(True))
  stats = neat.StatisticsReporter()
  population.add_reporter(stats)

  winner = population.run(
    main_game, #fitness function
    50 # maximum number of iterations to run
  )

  print('\nBest genome:\n{!s}'.format(winner))

def config_neat():
  local_dir = os.path.dirname(__file__)
  config_path = os.path.join(local_dir, "neat/config-feedforward.txt")
  run_neat(config_path)

def quit():
  pygame.quit()
  sys.exit()

def main():
  config_neat()

if __name__ == "__main__":
  main()
