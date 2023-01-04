import pygame
import random

from settings import *
from characters import *
from textures import Tile
from typing import Tuple
from camera import Camera

camera = Camera()


class Game:
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.tiles = pygame.sprite.Group()
        self.hero_sprite = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.electro_enemies = pygame.sprite.Group()
        self.alchemists = pygame.sprite.Group()
        self.tiles_arr = []
        for y in range(13):
            temp = []
            for x in range(20):
                num = random.randint(0, 1)
                if num:
                    tile = Tile("large hell stone", 100 * x, 100 * y, self.tiles, self.all_sprites)
                else:
                    tile = Tile("small hell stone", 100 * x, 100 * y, self.tiles, self.all_sprites)
                temp.append(tile)
            self.tiles_arr.append(temp)
        ElectroEnemy((500, 250), self.enemies, self.electro_enemies, self.all_sprites)
        Alchemist((250, 250), self.alchemists, self.all_sprites)
        self.hero = Hero((500, 500), self.hero_sprite, self.all_sprites)
        self.is_paused = False

    def draw_sprites(self, screen: pygame.Surface) -> None:
        """Drawing all tiles"""
        self.all_sprites.draw(screen)

    def update_alchemists_images(self) -> None:
        """Updating the alchemists picture"""
        if not self.is_paused:
            for sprite in self.alchemists:
                sprite.update_image()

    def update_heros_image(self) -> None:
        """Updating the heros image"""
        if not self.is_paused:
            for sprite in self.hero_sprite:
                sprite.update_image()

    def update_electro_enemies_image(self) -> None:
        if not self.is_paused:
            for sprite in self.electro_enemies:
                sprite.update_image()

    def is_free(self, position: Tuple[int, int]) -> bool:
        return self.tiles_arr[position[1] // 100][position[0] // 100].type in FREE_TYLES

    def is_hero_in_sight(self, enemy_position: Tuple[int, int], hero_position: Tuple[int, int]) -> bool:
        return abs(hero_position[0] - enemy_position[0]) <= 400 and abs(hero_position[1] - enemy_position[1]) <= 400

    def find_path_step(self, start: Tuple[int, int], target: Tuple[int, int]) -> Tuple[int, int]:
        step_size = 15
        if start[0] < target[0] and start[1] < target[1] and self.is_free((start[0] + step_size, start[1] + step_size)):
            return start[0] + step_size, start[1] + step_size
        elif start[0] == target[0] and start[1] < target[1] and self.is_free((start[0], start[1] + step_size)):
            return start[0], start[1] + step_size
        elif start[0] == target[0] and start[1] > target[1] and self.is_free((start[0], start[1] - step_size)):
            return start[0], start[1] - step_size
        elif start[0] < target[0] and start[1] == target[1] and self.is_free((start[0] + step_size, start[1])):
            return start[0] + step_size, start[1]
        elif start[0] > target[0] and start[1] == target[1] and self.is_free((start[0] - step_size, start[1])):
            return start[0] - step_size, start[1]
        elif start[0] > target[0] and start[1] > target[1] and self.is_free(
                (start[0] - step_size, start[1] - step_size)):
            return start[0] - step_size, start[1] - step_size
        elif start[0] < target[0] and start[1] < target[1] and self.is_free(
                (start[0] + step_size, start[1] + step_size)):
            return start[0] + step_size, start[1] + step_size
        elif start[0] < target[0] and start[1] > target[1] and self.is_free(
                (start[0] + step_size, start[1] - step_size)):
            return start[0] + step_size, start[1] - step_size
        elif start[0] > target[0] and start[1] < target[1] and self.is_free(
                (start[0] - step_size, start[1] + step_size)):
            return start[0] - step_size, start[1] + step_size
        return start

    def move_enemies(self) -> None:
        if not self.is_paused:
            for enemy in self.enemies:
                if self.is_hero_in_sight(enemy.get_position(), self.hero.get_position()):
                    next_position = self.find_path_step(enemy.get_position(), self.hero.get_position())
                    enemy.set_position(next_position)
                    enemy.is_running = True
                else:
                    enemy.is_running = False

    def can_enemy_attack(self, obj) -> bool:
        pass

    def update_enemies(self) -> None:
        pass

    def update(self) -> None:
        if not self.is_paused:
            self.hero.update_position()
            camera.update(self.hero)
            for sprite in self.all_sprites:
                camera.apply(sprite)
