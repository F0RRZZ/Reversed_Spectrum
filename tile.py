import pygame
import settings
import typing


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type: str, pos_x: int, pos_y: int, scale: typing.Tuple[int, int],  *groups):
        super().__init__(*groups)
        self.image = pygame.transform.scale(settings.TILE_IMAGES[tile_type], scale)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos_x, pos_y
        self.type = tile_type
        self.tile_type = tile_type
