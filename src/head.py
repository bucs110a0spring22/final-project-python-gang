import pygame


heads = [pygame.image.load(f'assets/CSHead{i}Trans.png') for i in range(1, 8)]


class Head(pygame.sprite.Sprite):
    def __init__(self, sprite_image, spawn_location, screen):
        super().__init__()
        self.x, self.y = sprite_image.get_size()
        n_img = pygame.transform.scale(sprite_image, (self.x / 2, self.y / 2))
        self.surf = n_img
        self.rect = self.surf.get_rect(center=spawn_location)
        screen.blit(self.surf, self.rect)

    def draw(self, screen):
        screen.blit(self.surf, self.rect)
