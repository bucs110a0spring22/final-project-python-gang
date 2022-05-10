import random

import pygame

from .head import Head, heads
from .pant import Pant, pants
from .shirt import Shirt, shirts
from .shoe import Shoe, shoes
from .rbutton import ranButton, buttons


class Controller:
    def __init__(self):  # Background
        self.window_width = 600
        self.window_height = 900
        pygame.init()
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        self.background = pygame.image.load('assets/BackgroundCS.png')
        pygame.display.set_caption("Random Outfit Generator")
        self.icon = pygame.image.load('assets/fashion.png')
        pygame.display.set_icon(self.icon)

    def generateOutfit(self):
        shoe = Shoe(random.choice(shoes), (self.window_width / 2, self.window_height / 2 + 250), self.screen)
        pant = Pant(random.choice(pants), (self.window_width / 2, self.window_height / 2 + 150), self.screen)
        shirt = Shirt(random.choice(shirts), (self.window_width / 2, self.window_height / 2 - 50), self.screen)
        head = Head(random.choice(heads), (self.window_width / 2 + 3, self.window_height / 2 - 190), self.screen)
        return shoe, pant, shirt, head

    def shoesOnly(self):
        shoe = Shoe(random.choice(shoes), (self.window_width / 2, self.window_height / 2 + 250), self.screen)
        return shoe

    def pantsOnly(self):
        pant = Pant(random.choice(pants), (self.window_width / 2, self.window_height / 2 + 150), self.screen)
        return pant

    def headsOnly(self):
        head = Head(random.choice(heads), (self.window_width / 2 + 3, self.window_height / 2 - 190), self.screen)
        return head

    def shirtsOnly(self):
        shirt = Shirt(random.choice(shirts), (self.window_width / 2, self.window_height / 2 - 50), self.screen)
        return shirt

    def mainLoop(self):
        shoe, pant, shirt, head = self.generateOutfit()
        shoe = self.shoesOnly()
        pant = self.pantsOnly()
        shirt = self.shirtsOnly()
        head = self.headsOnly()

        randomizebutton = ranButton(buttons, (self.window_width / 2+160, self.window_height / 2-380), self.screen)
        shoe_btn = ranButton(random.choice(shoes), (self.window_width / 2, self.window_height / 2 + 250), self.screen)
        shirt_btn = ranButton(random.choice(shirts), (self.window_width / 2, self.window_height / 2 - 50), self.screen)
        pant_btn = ranButton(random.choice(pants), (self.window_width / 2, self.window_height / 2 + 150), self.screen)
        head_btn = ranButton(random.choice(heads), (self.window_width / 2 + 3, self.window_height / 2 - 190), self.screen)

        running = True
        while running:
            self.screen.blit(self.background, (0, 0))

            shoe.draw(self.screen)
            pant.draw(self.screen)
            shirt.draw(self.screen)
            head.draw(self.screen)
            randomizebutton.draw(self.screen)
            pygame.display.update()

            events = pygame.event.get()
            mouse_pos = pygame.mouse.get_pos()

            for event in events:
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if randomizebutton.rect.collidepoint(mouse_pos):
                        shoe, pant, shirt, head = self.generateOutfit()
                    elif pant_btn.rect.collidepoint(mouse_pos):
                        pant = self.pantsOnly()
                    elif shirt_btn.rect.collidepoint(mouse_pos):
                        shirt = self.shirtsOnly()
                    elif head_btn.rect.collidepoint(mouse_pos):
                        head = self.headsOnly()
                    elif shoe_btn.rect.collidepoint(mouse_pos):
                        shoe = self.shoesOnly()