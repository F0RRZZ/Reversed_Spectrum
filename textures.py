import pygame

from image_loader import load_image


class GrassTexture(pygame.sprite.Sprite):
    image = pygame.transform.scale(load_image("grass.png"), (100, 100))

    def __init__(self, group, position: tuple):
        super().__init__(group)
        self.image = GrassTexture.image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position


class StoneTexture(pygame.sprite.Sprite):
    image = pygame.transform.scale(load_image("stone.png"), (100, 100))

    def __init__(self, group, position: tuple):
        super().__init__(group)
        self.image = StoneTexture.image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position


class LargeHellStoneTexture(pygame.sprite.Sprite):
    image = pygame.transform.scale(load_image("hell_stone2.png"), (100, 100))

    def __init__(self, group, position: tuple):
        super().__init__(group)
        self.image = LargeHellStoneTexture.image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position


class SmallHellStoneTexture(pygame.sprite.Sprite):
    image = pygame.transform.scale(load_image("hell_stone3.png"), (100, 100))

    def __init__(self, group, position: tuple):
        super().__init__(group)
        self.image = SmallHellStoneTexture.image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
