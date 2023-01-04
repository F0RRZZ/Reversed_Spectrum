import pygame

from settings import TILE_IMAGES, TILE_SIZE


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type: str, pos_x: int, pos_y: int, *groups):
        super().__init__(*groups)
        self.image = pygame.transform.scale(TILE_IMAGES[tile_type], TILE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos_x, pos_y
        self.type = tile_type
        self.tile_type = tile_type
