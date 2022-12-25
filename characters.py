import pygame
import random

from settings import *


class Hero(pygame.sprite.Sprite):
    right_standing_hero_images = HERO_IMAGES["right_standing"]
    left_standing_hero_images = [pygame.transform.flip(i, True, False) for i in right_standing_hero_images]
    right_attacking_hero_images = HERO_IMAGES["right_attacking"]
    left_attacking_hero_images = [pygame.transform.flip(i, True, False) for i in right_attacking_hero_images]
    right_walking_hero_images = HERO_IMAGES["right_walking"]
    left_walking_hero_images = [pygame.transform.flip(i, True, False) for i in right_walking_hero_images]

    def __init__(self, position: tuple, *groups):
        super().__init__(*groups)

        self.image = Hero.right_standing_hero_images[0]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

        pygame.time.set_timer(HERO_IMAGE_UPDATE_EVENT_TYPE, 200)
        pygame.time.set_timer(HERO_STEP_SOUND_EVENT_TYPE, 500)

        self.name = "Hero"
        self.inventory = 'inventory'
        self.direction = 'right'
        self.attacking = False
        self.walking = False

    def get_position(self) -> tuple:
        return self.rect.x, self.rect.y

    def set_position(self, position: tuple):
        self.rect.x, self.rect.y = position

    def standing_hero_animation(self):
        """Updating the picture if the hero stands"""
        img_by_dir = {'left': Hero.left_standing_hero_images, 'right': Hero.right_standing_hero_images}
        try:
            image_index = img_by_dir[self.direction].index(self.image)
            self.image = img_by_dir[self.direction][(image_index + 1) % 5]
        except ValueError:
            self.image = img_by_dir[self.direction][0]

    def walking_hero_animation(self):
        """Updating the picture if the hero walks"""
        img_by_dir = {'left': Hero.left_walking_hero_images, 'right': Hero.right_walking_hero_images}
        try:
            image_index = img_by_dir[self.direction].index(self.image)
            self.image = img_by_dir[self.direction][(image_index + 1) % 6]
        except ValueError:
            self.image = img_by_dir[self.direction][0]

    def attacking_hero_animation(self):
        """Updating the picture if the hero attacks"""
        img_by_dir = {'left': Hero.left_attacking_hero_images, 'right': Hero.right_attacking_hero_images}
        image_index = img_by_dir[self.direction].index(self.image)
        self.image = img_by_dir[self.direction][image_index + 1]
        if image_index + 1 == 5:
            self.attacking = False

    def update_image(self):
        """Updating the heros image"""
        if not self.attacking:
            if not self.walking:
                self.standing_hero_animation()
            else:
                self.walking_hero_animation()
            pygame.time.set_timer(HERO_IMAGE_UPDATE_EVENT_TYPE, 200)
        else:
            self.attacking_hero_animation()

    def change_direction(self, direction: str):
        """Changing the direction if the hero and his image"""
        self.direction = direction
        if self.direction == 'right' and self.image not in Hero.right_walking_hero_images:
            self.image = Hero.right_walking_hero_images[0]
        elif self.direction == 'left' and self.image not in Hero.left_walking_hero_images:
            self.image = Hero.left_walking_hero_images[0]

    def update_position(self):
        if not self.attacking:
            position = self.get_position()
            keys = pygame.key.get_pressed()
            self.walking = any(keys)

            if keys[pygame.K_a]:
                self.change_direction('left')
            elif keys[pygame.K_d]:
                self.change_direction('right')

            if keys[pygame.K_w] and keys[pygame.K_d]:
                self.set_position((position[0] + 10, position[1] - 10))
            elif keys[pygame.K_w] and keys[pygame.K_a]:
                self.set_position((position[0] - 10, position[1] - 10))
            elif keys[pygame.K_s] and keys[pygame.K_d]:
                self.set_position((position[0] + 10, position[1] + 10))
            elif keys[pygame.K_s] and keys[pygame.K_a]:
                self.set_position((position[0] - 10, position[1] + 10))
            elif keys[pygame.K_d]:
                self.set_position((position[0] + 10, position[1]))
            elif keys[pygame.K_a]:
                self.set_position((position[0] - 10, position[1]))
            elif keys[pygame.K_w]:
                self.set_position((position[0], position[1] - 10))
            elif keys[pygame.K_s]:
                self.set_position((position[0], position[1] + 10))

    def attack(self):
        """Animating the heros attack"""
        self.attacking = True
        HERO_SOUNDS[f"attack{random.randint(1, 2)}"].play()
        if self.direction == 'right':
            self.image = Hero.right_attacking_hero_images[0]
        elif self.direction == 'left':
            self.image = Hero.left_attacking_hero_images[0]
        pygame.time.set_timer(HERO_IMAGE_UPDATE_EVENT_TYPE, 80)


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
