import pygame
import random

from settings import *
from typing import Tuple


class Hero(pygame.sprite.Sprite):
    right_standing_hero_images = HERO_IMAGES["right_standing"]
    left_standing_hero_images = [pygame.transform.flip(i, True, False) for i in right_standing_hero_images]
    right_attacking_hero_images = HERO_IMAGES["right_attacking"]
    left_attacking_hero_images = [pygame.transform.flip(i, True, False) for i in right_attacking_hero_images]
    right_walking_hero_images = HERO_IMAGES["right_walking"]
    left_walking_hero_images = [pygame.transform.flip(i, True, False) for i in right_walking_hero_images]

    def __init__(self, position: Tuple[int, int], *groups):
        super().__init__(*groups)

        self.image = Hero.right_standing_hero_images[0]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

        pygame.time.set_timer(HERO_IMAGE_UPDATE_EVENT_TYPE, 200)  # timer for updating heros image
        pygame.time.set_timer(HERO_STEP_SOUND_EVENT_TYPE, 500)  # timer for turning on the sound of footsteps

        self.name = "Hero"
        self.inventory = 'inventory'
        self.direction = 'right'
        self.health = 100
        self.mana = 100
        self.is_attacking = False
        self.is_walking = False

    def get_position(self) -> Tuple[int, int]:
        return self.rect.x, self.rect.y

    def set_position(self, position: Tuple[int, int]):
        self.rect.x, self.rect.y = position

    def standing_animation(self) -> None:
        """Updating the picture if the hero stands"""
        img_by_dir = {'left': Hero.left_standing_hero_images, 'right': Hero.right_standing_hero_images}
        try:
            image_index = img_by_dir[self.direction].index(self.image)
            self.image = img_by_dir[self.direction][(image_index + 1) % 5]
        except ValueError:
            # if current image not in the list with hero standing images
            self.image = img_by_dir[self.direction][0]

    def walking_animation(self) -> None:
        """Updating the picture if the hero walks"""
        img_by_dir = {'left': Hero.left_walking_hero_images, 'right': Hero.right_walking_hero_images}
        try:
            image_index = img_by_dir[self.direction].index(self.image)
            self.image = img_by_dir[self.direction][(image_index + 1) % 6]
        except ValueError:
            # if current image not in the list with hero walking images
            self.image = img_by_dir[self.direction][0]

    def attacking_animation(self) -> None:
        """Updating the picture if the hero attacks"""
        img_by_dir = {'left': Hero.left_attacking_hero_images, 'right': Hero.right_attacking_hero_images}
        image_index = img_by_dir[self.direction].index(self.image)
        self.image = img_by_dir[self.direction][image_index + 1]
        if image_index + 1 == 5:
            self.is_attacking = False

    def update_image(self) -> None:
        """Updating the heros image"""
        if not self.is_attacking:
            if not self.is_walking:
                self.standing_animation()
            else:
                self.walking_animation()
            pygame.time.set_timer(HERO_IMAGE_UPDATE_EVENT_TYPE, 200)
        else:
            self.attacking_animation()

    def change_direction(self, direction: str) -> None:
        """Changing the direction if the hero and his image"""
        self.direction = direction
        if self.direction == 'right' and self.image not in Hero.right_walking_hero_images:
            self.image = Hero.right_walking_hero_images[0]
        elif self.direction == 'left' and self.image not in Hero.left_walking_hero_images:
            self.image = Hero.left_walking_hero_images[0]

    def update_position(self) -> None:
        if not self.is_attacking:
            position = self.get_position()
            keys = pygame.key.get_pressed()
            self.is_walking = any(keys)

            if keys[pygame.K_a]:
                self.change_direction('left')
            elif keys[pygame.K_d]:
                self.change_direction('right')

            if keys[pygame.K_w] and keys[pygame.K_d]:
                self.set_position((position[0] + HERO_MOVE_SPEED, position[1] - HERO_MOVE_SPEED))
            elif keys[pygame.K_w] and keys[pygame.K_a]:
                self.set_position((position[0] - HERO_MOVE_SPEED, position[1] - HERO_MOVE_SPEED))
            elif keys[pygame.K_s] and keys[pygame.K_d]:
                self.set_position((position[0] + HERO_MOVE_SPEED, position[1] + HERO_MOVE_SPEED))
            elif keys[pygame.K_s] and keys[pygame.K_a]:
                self.set_position((position[0] - HERO_MOVE_SPEED, position[1] + HERO_MOVE_SPEED))
            elif keys[pygame.K_d]:
                self.set_position((position[0] + HERO_MOVE_SPEED, position[1]))
            elif keys[pygame.K_a]:
                self.set_position((position[0] - HERO_MOVE_SPEED, position[1]))
            elif keys[pygame.K_w]:
                self.set_position((position[0], position[1] - HERO_MOVE_SPEED))
            elif keys[pygame.K_s]:
                self.set_position((position[0], position[1] + HERO_MOVE_SPEED))

    def attack(self) -> None:
        """Switches hero mode to attack"""
        self.is_attacking = True
        self.play_attack_sound()
        if self.direction == 'right':
            self.image = Hero.right_attacking_hero_images[0]
        elif self.direction == 'left':
            self.image = Hero.left_attacking_hero_images[0]
        pygame.time.set_timer(HERO_IMAGE_UPDATE_EVENT_TYPE, 80)

    @staticmethod
    def play_attack_sound() -> None:
        HERO_SOUNDS[f"attack{random.randint(1, 2)}"].play()


class Alchemist(pygame.sprite.Sprite):
    images = ALCHEMIST_IMAGES['right']

    def __init__(self, position: tuple, *groups):
        super().__init__(*groups)

        self.image = Alchemist.images[0]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

        pygame.time.set_timer(ALCHEMIST_EVENT_TYPE, 700)

        self.name = 'Alchemist'
        self.skills = 'High'

    def update_image(self):
        self.image = Alchemist.images[Alchemist.images.index(self.image) - 1]


class ElectroEnemy(pygame.sprite.Sprite):
    images_standing_right = ELECTRO_ENEMY_IMAGES["right_standing"]
    images_standing_left =[pygame.transform.flip(i, True, False) for i in images_standing_right]
    images_running_right = ELECTRO_ENEMY_IMAGES["right_running"]
    images_running_left = [pygame.transform.flip(i, True, False) for i in images_running_right]

    def __init__(self, position: Tuple[int, int], *groups):
        super().__init__(*groups)

        self.image = ElectroEnemy.images_standing_right[0]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.direction = 'left'
        self.is_running = False

        pygame.time.set_timer(ELECTRO_ENEMY_EVENT_TYPE, 120)
        pygame.time.set_timer(ELECTRO_ENEMY_MOVE_EVENT_TYPE, 100)

    def get_position(self) -> Tuple[int, int]:
        return self.rect.x, self.rect.y

    def set_position(self, position: Tuple[int, int]) -> None:
        self.direction = 'left' if self.rect.x > position[0] else 'right'
        self.rect.x, self.rect.y = position

    def standing_animation(self) -> None:
        images = {'left': ElectroEnemy.images_standing_left, 'right': ElectroEnemy.images_standing_right}
        try:
            image_index = (images[self.direction].index(self.image) + 1) % 8
            self.image = images[self.direction][image_index]
        except ValueError:
            # if current image not in the list with enemy standing images
            self.image = images[self.direction][0]

    def running_animation(self) -> None:
        images = {'left': ElectroEnemy.images_running_left, 'right': ElectroEnemy.images_running_right}
        try:
            image_index = (images[self.direction].index(self.image) + 1) % 6
            self.image = images[self.direction][image_index]
        except ValueError:
            self.image = images[self.direction][0]

    def attacking_animation(self) -> None:
        pass

    def update_image(self) -> None:
        if self.is_running:
            self.running_animation()
        else:
            self.standing_animation()
