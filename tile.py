import pygame
import loaders
import typing


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type: str, pos_x: int, pos_y: int, scale: typing.Tuple[int, int],  *groups):
        super().__init__(*groups)
        self.image = pygame.transform.scale(loaders.load_image(f"{tile_type}.png"), scale)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos_x, pos_y
        self.type = tile_type
        self.tile_type = tile_type
