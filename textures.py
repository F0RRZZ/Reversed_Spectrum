import pygame

from image_loader import load_image
from settings import TILE_IMAGES


class Tile(pygame.sprite.Sprite):
    def __init__(self, group, tile_type: str, pos_x: int, pos_y: int):
        super().__init__(group)
        self.image = pygame.transform.scale(TILE_IMAGES[tile_type], (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos_x, pos_y
        self.type = tile_type
