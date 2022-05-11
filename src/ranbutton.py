import pygame

buttons = pygame.image.load('assets/RandomButton.png')


class ranButton(pygame.sprite.Sprite):
    def __init__(self, sprite_image, spawn_location, screen):
        super().__init__()
        self.x, self.y = sprite_image.get_size()
        n_img = pygame.transform.scale(sprite_image, (self.x / 3, self.y / 3))
        self.surf = n_img
        self.rect = self.surf.get_rect(center=spawn_location)
        self.clicked = False
        screen.blit(self.surf, self.rect)

    def draw(self, screen):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.surf, self.rect)

        return action