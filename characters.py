import pygame

from settings import *
from image_loader import load_image


class Hero(pygame.sprite.Sprite):
    right_standing_hero_images = [pygame.transform.scale(load_image("hero1.png"), (150, 150)),
                                  pygame.transform.scale(load_image("hero2.png"), (150, 150)),
                                  pygame.transform.scale(load_image("hero3.png"), (150, 150)),
                                  pygame.transform.scale(load_image("hero2.png"), (150, 150)),
                                  pygame.transform.scale(load_image("hero1.png"), (150, 150))]
    left_standing_hero_images = [pygame.transform.flip(i, True, False) for i in right_standing_hero_images]
    right_attacking_hero_images = [pygame.transform.scale(load_image("hero1.png"), (150, 150)),
                                   pygame.transform.scale(load_image("attacking_hero1.png"), (150, 174)),
                                   pygame.transform.scale(load_image("attacking_hero2.png"), (300, 156)),
                                   pygame.transform.scale(load_image("attacking_hero3.png"), (150, 150)),
                                   pygame.transform.scale(load_image("attacking_hero4.png"), (150, 150)),
                                   pygame.transform.scale(load_image("attacking_hero5.png"), (150, 150))]
    left_attacking_hero_images = [pygame.transform.flip(i, True, False) for i in right_attacking_hero_images]
    right_walking_hero_images = [pygame.transform.scale(load_image("walking_hero1.png"), (150, 150)),
                                 pygame.transform.scale(load_image("walking_hero2.png"), (150, 150)),
                                 pygame.transform.scale(load_image("walking_hero3.png"), (150, 150)),
                                 pygame.transform.scale(load_image("walking_hero4.png"), (150, 150)),
                                 pygame.transform.scale(load_image("walking_hero5.png"), (150, 150)),
                                 pygame.transform.scale(load_image("walking_hero6.png"), (150, 150))]
    left_walking_hero_images = [pygame.transform.flip(i, True, False) for i in right_walking_hero_images]

    def __init__(self, group, position: tuple):
        super().__init__(group)

        self.image = Hero.right_standing_hero_images[0]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

        pygame.time.set_timer(HERO_EVENT_TYPE, 200)

        self.name = "Hero"
        self.inventory = 'inventory'
        self.direction = 'right'
        self.attacking = False
        self.walking = False

    def get_position(self):
        return self.rect.x, self.rect.y

    def set_position(self, position: tuple):
        self.rect.x, self.rect.y = position

    def update_image(self):
        if not self.attacking:
            if not self.walking:
                if self.image not in Hero.right_standing_hero_images and self.image not in Hero.left_standing_hero_images:
                    if self.direction == 'right':
                        self.image = Hero.right_standing_hero_images[0]
                    elif self.direction == 'left':
                        self.image = Hero.left_standing_hero_images[0]
                else:
                    if self.direction == 'right':
                        self.image = Hero.right_standing_hero_images[(Hero.right_standing_hero_images.index(self.image) + 1) % 5]
                    elif self.direction == 'left':
                        self.image = Hero.left_standing_hero_images[(Hero.left_standing_hero_images.index(self.image) + 1) % 5]
            else:
                if self.image not in Hero.right_walking_hero_images and self.image not in Hero.left_walking_hero_images:
                    if self.direction == 'right':
                        self.image = Hero.right_walking_hero_images[0]
                    elif self.direction == 'left':
                        self.image = Hero.left_walking_hero_images[0]
                else:
                    if self.direction == 'right':
                        self.image = Hero.right_walking_hero_images[(Hero.right_walking_hero_images.index(self.image) + 1) % 6]
                    elif self.direction == 'left':
                        self.image = Hero.left_walking_hero_images[(Hero.left_walking_hero_images.index(self.image) + 1) % 6]
            pygame.time.set_timer(HERO_EVENT_TYPE, 200)
        else:
            if self.direction == 'right':
                self.image = Hero.right_attacking_hero_images[(Hero.right_attacking_hero_images.index(self.image) + 1) % 6]
                if Hero.right_attacking_hero_images.index(self.image) == 5:
                    self.attacking = False
            elif self.direction == 'left':
                self.image = Hero.left_attacking_hero_images[(Hero.left_attacking_hero_images.index(self.image) + 1) % 6]
                if Hero.left_attacking_hero_images.index(self.image) == 5:
                    self.attacking = False

    def update_position(self):
        if not self.attacking:
            position = self.get_position()
            keys = pygame.key.get_pressed()
            self.walking = any(keys)
            if keys[pygame.K_w] and keys[pygame.K_d]:
                self.set_position((position[0] + 10, position[1] - 10))
                self.direction = 'right'
                if self.image not in Hero.right_walking_hero_images:
                    self.image = Hero.right_walking_hero_images[0]
            elif keys[pygame.K_w] and keys[pygame.K_a]:
                self.set_position((position[0] - 10, position[1] - 10))
                self.direction = 'left'
                if self.image not in Hero.right_walking_hero_images:
                    self.image = Hero.left_walking_hero_images[0]
            elif keys[pygame.K_s] and keys[pygame.K_d]:
                self.set_position((position[0] + 10, position[1] + 10))
                self.direction = 'right'
                if self.image not in Hero.right_walking_hero_images:
                    self.image = Hero.right_walking_hero_images[0]
            elif keys[pygame.K_s] and keys[pygame.K_a]:
                self.set_position((position[0] - 10, position[1] + 10))
                self.direction = 'left'
                if self.image not in Hero.right_walking_hero_images:
                    self.image = Hero.left_walking_hero_images[0]
            elif keys[pygame.K_d]:
                self.set_position((position[0] + 10, position[1]))
                self.direction = 'right'
                if self.image not in Hero.right_walking_hero_images:
                    self.image = Hero.right_walking_hero_images[0]
            elif keys[pygame.K_a]:
                self.set_position((position[0] - 10, position[1]))
                self.direction = 'left'
                if self.image not in Hero.left_walking_hero_images:
                    self.image = Hero.left_standing_hero_images[0]
            elif keys[pygame.K_w]:
                self.set_position((position[0], position[1] - 10))
            elif keys[pygame.K_s]:
                self.set_position((position[0], position[1] + 10))

    def attack(self):
        self.attacking = True
        if self.direction == 'right':
            self.image = Hero.right_attacking_hero_images[0]
        elif self.direction == 'left':
            self.image = Hero.left_attacking_hero_images[0]
        pygame.time.set_timer(HERO_EVENT_TYPE, 80)


class Alchemist(pygame.sprite.Sprite):
    images = [pygame.transform.scale(load_image("alchemist.png"), (100, 100)),
              pygame.transform.scale(load_image("alchemist2.png"), (100, 100))]

    def __init__(self, group, position: tuple):
        super().__init__(group)

        self.image = Alchemist.images[0]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

        pygame.time.set_timer(ALCHEMIST_EVENT_TYPE, 700)

        self.name = 'Alchemist'
        self.skills = 'High'

    def update_image(self):
        self.image = Alchemist.images[Alchemist.images.index(self.image) - 1]
