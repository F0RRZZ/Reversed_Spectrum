import pygame
import settings
import characters
import typing
import camera
import tools
import loaders


camera_obj = camera.Camera()


class Game:
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.tiles = pygame.sprite.Group()
        self.hero_sprite = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.electro_enemies = pygame.sprite.Group()
        self.alchemists = pygame.sprite.Group()
        self.tiles_arr = loaders.load_map(1, self.all_sprites, self.tiles)
        self.hero = characters.Hero((500, 500), self.hero_sprite)
        characters.ElectroEnemy((500, 250), self.hero, self.enemies, self.electro_enemies, self.all_sprites)
        characters.ElectroEnemy((1000, 1000), self.hero, self.enemies, self.electro_enemies, self.all_sprites)
        characters.Alchemist((250, 250), self.alchemists, self.all_sprites)
        self.is_paused = False

    def draw_sprites(self, screen: pygame.Surface) -> None:
        """Drawing all tiles"""
        self.all_sprites.draw(screen)

    def hero_attack(self):
        for enemy in self.enemies:
            if self.hero.rect.colliderect(enemy.rect):
                self.hero.hit(enemy)
        self.hero.attack()

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

    def is_free(self, position: typing.Tuple[int, int]) -> bool:
        """
        Сhecks if the next cell is free.
        :param position: characters position
        """
        return self.tiles_arr[position[1] // 100][position[0] // 100].type in settings.FREE_TYLES

    @staticmethod
    def is_hero_in_sight(enemy_position: typing.Tuple[int, int], hero_position: typing.Tuple[int, int]) -> bool:
        """
        Checks whether the hero is in the enemy's sight.
        :param enemy_position: enemy position
        :param hero_position: hero position
        """
        return abs(hero_position[0] - enemy_position[0]) <= 400 and abs(hero_position[1] - enemy_position[1]) <= 400

    def find_path_step(self, start: typing.Tuple[int, int], target: typing.Tuple[int, int]) -> typing.Tuple[int, int]:
        """
        Finds the way to the hero.
        :param start: enemies position
        :param target: targets position
        """
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

    def can_enemy_attack(self, enemy: pygame.sprite.Sprite) -> None:
        """
        Checks if the enemy can hit the hero.
        :param enemy: enemy sprite
        """
        if enemy.rect.colliderect(self.hero.rect):
            enemy.attack()
            enemy.is_running = False
        else:
            enemy.is_running = True

    def move_enemies(self) -> None:
        """Moves enemies"""
        try:
            if not self.is_paused:
                for enemy in self.enemies:
                    if self.is_hero_in_sight(enemy.get_position(), self.hero.get_position()) and\
                            not enemy.is_attacking and not enemy.is_damaged:
                        next_position = self.find_path_step(enemy.get_position(), self.hero.get_position())
                        enemy.set_position(next_position)
                        self.can_enemy_attack(enemy)
                    else:
                        enemy.is_running = False
                        enemy.is_standing = True
        except Exception:
            print("Unknown error.")

    def update_enemies(self) -> None:
        pass

    def game_update(self, screen: pygame.Surface) -> None:
        """Games update"""
        if not self.is_paused:
            self.hero.update_position()
            camera_obj.update(self.hero)
            for sprite in self.all_sprites:
                camera_obj.apply(sprite)
            for hero in self.hero_sprite:
                camera_obj.apply(hero)

    def render(self, screen: pygame.Surface):
        self.all_sprites.draw(screen)
        self.hero_sprite.draw(screen)
        self.game_update(screen)
        tools.stats_drawer(screen, self.hero.health, self.hero.mana)
