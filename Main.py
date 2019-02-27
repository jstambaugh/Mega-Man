import pygame
from pygame.locals import*
import Settings
import Mega_Man

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((Settings.WIDTH, Settings.HEIGHT))
background = pygame.image.load("GutsmanStage.png")
background_rect = screen.get_rect()
pygame.display.set_caption("Mega Man")
player = Mega_Man.Player(0,150)

sprite_list = pygame.sprite.Group()
player.rect.x = 0
player.rect.y = 150
sprite_list.add(player)
ground = 250
clock = pygame.time.Clock()

# variables that will be changed depending on if the character is moving or not
change_x = 0
change_y = 0

Game = True
while Game:
  for event in pygame.event.get():
    if event.type == QUIT:
      Game = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            change_x = 3
            player.direction = "Right"
        if event.key == pygame.K_LEFT:
            change_x = -3
            player.direction = "Left"
        if event.key == pygame.K_SPACE:
            
        if event.key == pygame.K_f:
            player.shooting = "True"

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            change_x = 0
            player.direction = "None-right"
        if event.key == pygame.K_LEFT:
            change_x = 0
            player.direction = "None-left"
        if event.key == pygame.K_f:
            player.shooting = "False"

  player.rect.x += change_x
  player.rect.y += change_y
  screen.fill(Settings.WHITE)
  sprite_list.update()
  sprite_list.draw(screen)
  clock.tick(Settings.FPS)
  pygame.display.update()
  pygame.display.flip()

pygame.quit()