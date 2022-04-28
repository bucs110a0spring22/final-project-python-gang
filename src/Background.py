import pygame 
import sys 

screen = pygame.display.set_mode((1080, 1920))
pygame.display.set_caption("Random Clothing Generator!")

background = pygame.image.load('images/background.png')

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  
  screen.fill((0, 0, 0))
  screen.blit(background, (0, 0))
  
  pygame.display.update()
                        