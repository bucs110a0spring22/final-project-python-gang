import pygame

from pygame import mixer
from src import shirt
from .shirt import Shirt, shirts
from src import shirt
from .pant import Pant, pants
from src import shoe
from .shoe import Shoe, shoes
from src import head
from .head import Head, heads
import random


class Controller:
    def __init__(self):    #Background
        self.window_width = 600
        self.window_height = 900
        pygame.init()
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        self.background = pygame.image.load('assets/AdobeBG4.png')
        pygame.display.set_caption("Random Clothing Generator")
        self.icon = pygame.image.load('assets/fashion.png')
        pygame.display.set_icon(self.icon)

    def generateOutfit(self):
        shoe = Shoe(random.choice(shoes), (self.window_width/2, self.window_height/2+250), self.screen)
        pant = Pant(random.choice(pants), (self.window_width/2, self.window_height/2+150), self.screen)
        shirt = Shirt(random.choice(shirts), (self.window_width/2, self.window_height/2-50), self.screen)
        head = Head(random.choice(heads), (self.window_width/2+3, self.window_height/2-190), self.screen)
        return shoe, pant, shirt, head

    def mainLoop(self):
        shoe, pant, shirt, head = self.generateOutfit()

        running = True
        while running:
            self.screen.blit(self.background, (0,0))

            shoe.draw(self.screen)
            pant.draw(self.screen)
            shirt.draw(self.screen)
            head.draw(self.screen)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    shoe, pant, shirt, head = self.generateOutfit()

     
