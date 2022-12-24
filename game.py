import pygame
import random

from settings import *
from characters import *
from textures import Tile
from camera import Camera


camera = Camera()


class Game:
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.tiles = pygame.sprite.Group()
        self.hero_sprite = pygame.sprite.Group()
        self.alchemists = pygame.sprite.Group()
        for y in range(13):
            for x in range(20):
                num = random.randint(0, 1)
                if num:
                    Tile("large hell stone", 100 * x, 100 * y, self.tiles, self.all_sprites)
                else:
                    Tile("small hell stone", 100 * x, 100 * y, self.tiles, self.all_sprites)
        self.hero = Hero((500, 500), self.hero_sprite, self.all_sprites)
        Alchemist((250, 250), self.alchemists, self.all_sprites)

    def draw_sprites(self, screen: pygame.Surface):
        """Drawing all tiles"""
        self.all_sprites.draw(screen)

    def update_alchemists_images(self):
        """Updating the alchemists picture"""
        for sprite in self.alchemists:
            sprite.update_image()

    def update_heros_image(self):
        """Updating the heros image"""
        for sprite in self.hero_sprite:
            sprite.update_image()

    def update(self):
        self.hero.update_position()
        camera.update(self.hero)
        for sprite in self.all_sprites:
            camera.apply(sprite)
