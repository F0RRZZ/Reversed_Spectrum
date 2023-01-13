import pygame
import random
import settings
import typing
import inventory


class Hero(pygame.sprite.Sprite):
    right_standing_images = settings.HERO_IMAGES["right_standing"]
    left_standing_images = [pygame.transform.flip(i, True, False) for i in right_standing_images]
    right_attacking_images = settings.HERO_IMAGES["right_attacking"]
    left_attacking_images = [pygame.transform.flip(i, True, False) for i in right_attacking_images]
    right_walking_images = settings.HERO_IMAGES["right_walking"]
    left_walking_images = [pygame.transform.flip(i, True, False) for i in right_walking_images]
    right_damaged_images = settings.HERO_IMAGES["right_damaged"]
    left_damaged_images = [pygame.transform.flip(i, True, False) for i in right_damaged_images]

    def __init__(self, position: typing.Tuple[int, int], inventory_obj: inventory.Inventory, *groups):
        super().__init__(*groups)

        self.image = Hero.right_standing_images[0]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

        pygame.time.set_timer(settings.HERO_IMAGE_UPDATE_EVENT_TYPE, 200)  # timer for updating heros image
        pygame.time.set_timer(settings.HERO_STEP_SOUND_EVENT_TYPE, 500)  # timer for turning on the sound of footsteps

        self.inventory = inventory_obj
        self.damage = self.inventory.weapon.damage
        self.health = 100
        self.defence = self.inventory.get_defence_value()
        self.mana = 100

        self.direction = 'right'
        self.is_attacking = False
        self.is_walking = False
        self.is_damaged = False
        self.is_died = False

    def get_position(self) -> typing.Tuple[int, int]:
        return self.rect.x, self.rect.y

    def set_position(self, position: typing.Tuple[int, int]):
        self.rect.x, self.rect.y = position

    @staticmethod
    def play_attack_sound() -> None:
        settings.HERO_SOUNDS[f"attack{random.randint(1, 2)}"].play()

    def hit(self, target) -> None:
        target.get_damage(self.damage)

    def update_inventory(self, new_inventory: inventory.Inventory):
        self.inventory = new_inventory
        self.damage = self.inventory.weapon.damage
        self.defence = self.inventory.get_defence_value()

    def standing_animation(self) -> None:
        """Updating the picture if the hero stands"""
        img_by_dir = {'left': Hero.left_standing_images, 'right': Hero.right_standing_images}
        try:
            image_index = img_by_dir[self.direction].index(self.image)
            self.image = img_by_dir[self.direction][(image_index + 1) % 5]
        except ValueError:
            # if current image not in the list with hero standing images
            self.image = img_by_dir[self.direction][0]

    def walking_animation(self) -> None:
        """Updating the picture if the hero walks"""
        img_by_dir = {'left': Hero.left_walking_images, 'right': Hero.right_walking_images}
        try:
            image_index = img_by_dir[self.direction].index(self.image)
            self.image = img_by_dir[self.direction][(image_index + 1) % 6]
        except ValueError:
            # if current image not in the list with hero walking images
            self.image = img_by_dir[self.direction][0]

    def attacking_animation(self) -> None:
        """Updating the picture if the hero attacks"""
        img_by_dir = {'left': Hero.left_attacking_images, 'right': Hero.right_attacking_images}
        image_index = img_by_dir[self.direction].index(self.image)
        self.image = img_by_dir[self.direction][image_index + 1]
        if image_index + 1 == 5:
            self.is_attacking = False

    def damaged_animation(self) -> None:
        images = {'left': Hero.left_damaged_images, 'right': Hero.right_damaged_images}
        try:
            image_index = images[self.direction].index(self.image) + 1
            self.image = images[self.direction][image_index]
            if image_index == len(Hero.right_damaged_images) - 1:
                self.is_damaged = False
        except ValueError:
            self.is_damaged = False

    def change_direction(self, direction: str) -> None:
        """Changing the direction if the hero and his image"""
        self.direction = direction
        if self.direction == 'right' and self.image not in Hero.right_walking_images:
            self.image = Hero.right_walking_images[0]
        elif self.direction == 'left' and self.image not in Hero.left_walking_images:
            self.image = Hero.left_walking_images[0]

    def get_damage(self, damage: int) -> None:
        if not self.is_died:
            self.is_damaged = True
            self.health -= damage * (1 - self.defence)
            self.image = {'left': Hero.left_damaged_images,
                          'right': Hero.right_damaged_images}.get(self.direction)[0]
            if self.health <= 0:
                self.is_died = True

    def update_position(self) -> None:
        if not self.is_attacking and not self.is_damaged:
            position = self.get_position()
            keys = pygame.key.get_pressed()
            self.is_walking = any(keys)

            if keys[pygame.K_a]:
                self.change_direction('left')
            elif keys[pygame.K_d]:
                self.change_direction('right')

            if keys[pygame.K_w] and keys[pygame.K_d]:
                self.set_position((position[0] + settings.HERO_MOVE_SPEED, position[1] - settings.HERO_MOVE_SPEED))
            elif keys[pygame.K_w] and keys[pygame.K_a]:
                self.set_position((position[0] - settings.HERO_MOVE_SPEED, position[1] - settings.HERO_MOVE_SPEED))
            elif keys[pygame.K_s] and keys[pygame.K_d]:
                self.set_position((position[0] + settings.HERO_MOVE_SPEED, position[1] + settings.HERO_MOVE_SPEED))
            elif keys[pygame.K_s] and keys[pygame.K_a]:
                self.set_position((position[0] - settings.HERO_MOVE_SPEED, position[1] + settings.HERO_MOVE_SPEED))
            elif keys[pygame.K_d]:
                self.set_position((position[0] + settings.HERO_MOVE_SPEED, position[1]))
            elif keys[pygame.K_a]:
                self.set_position((position[0] - settings.HERO_MOVE_SPEED, position[1]))
            elif keys[pygame.K_w]:
                self.set_position((position[0], position[1] - settings.HERO_MOVE_SPEED))
            elif keys[pygame.K_s]:
                self.set_position((position[0], position[1] + settings.HERO_MOVE_SPEED))

    def attack(self) -> None:
        """Switches hero mode to attack"""
        self.is_attacking = True
        self.play_attack_sound()
        if self.direction == 'right':
            self.image = Hero.right_attacking_images[0]
        elif self.direction == 'left':
            self.image = Hero.left_attacking_images[0]
        pygame.time.set_timer(settings.HERO_IMAGE_UPDATE_EVENT_TYPE, 80)

    def update_image(self) -> None:
        """Updating the heros image"""
        if not self.is_damaged:
            if not self.is_attacking:
                if not self.is_walking:
                    self.standing_animation()
                else:
                    self.walking_animation()
                pygame.time.set_timer(settings.HERO_IMAGE_UPDATE_EVENT_TYPE, 200)
            else:
                self.attacking_animation()
        else:
            self.damaged_animation()


class Alchemist(pygame.sprite.Sprite):
    images = settings.ALCHEMIST_IMAGES['right']

    def __init__(self, position: tuple, *groups):
        super().__init__(*groups)

        self.image = Alchemist.images[0]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

        pygame.time.set_timer(settings.ALCHEMIST_EVENT_TYPE, 700)

        self.name = 'Alchemist'
        self.skills = 'High'

    def update_image(self):
        self.image = Alchemist.images[Alchemist.images.index(self.image) - 1]


class Enemy(pygame.sprite.Sprite):
    def __init__(self, position: typing.Tuple[int, int], target: Hero, *groups):
        super().__init__(*groups)

        self.image = self.images_standing_right[0]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.direction = 'left'
        self.is_running = False
        self.is_attacking = False
        self.is_damaged = False
        self.is_died = False

        self.target = target

        pygame.time.set_timer(settings.ELECTRO_ENEMY_EVENT_TYPE, 120)
        pygame.time.set_timer(settings.ELECTRO_ENEMY_MOVE_EVENT_TYPE, 100)

    def get_position(self) -> typing.Tuple[int, int]:
        return self.rect.x, self.rect.y

    def set_position(self, position: typing.Tuple[int, int]) -> None:
        self.direction = 'left' if self.rect.x > position[0] else 'right'
        self.rect.x, self.rect.y = position

    def hit(self, hero: Hero) -> None:
        hero.get_damage(self.damage)

    def get_damage(self, damage: int) -> None:
        if not self.is_died:
            self.is_damaged = True
            self.health -= damage
            self.image = {'left': self.images_damaged_left,
                          'right': self.images_damaged_right}.get(self.direction)[0]
            if self.health <= 0:
                self.is_died = True

    def standing_animation(self) -> None:
        images = {'left': self.images_standing_left, 'right': self.images_standing_right}
        try:
            image_index = (images[self.direction].index(self.image) + 1) % len(images['left'])
            self.image = images[self.direction][image_index]
        except ValueError:
            # if current image not in the list with enemy standing images
            self.image = images[self.direction][0]

    def running_animation(self) -> None:
        images = {'left': self.images_running_left, 'right': self.images_running_right}
        try:
            image_index = (images[self.direction].index(self.image) + 1) % len(images['left'])
            self.image = images[self.direction][image_index]
        except ValueError:
            self.image = images[self.direction][0]

    def attacking_animation(self) -> None:
        images = {'left': self.images_attacking_left, 'right': self.images_attacking_right}
        image_index = 0
        try:
            image_index = images[self.direction].index(self.image)
            self.image = images[self.direction][image_index + 1]
        except ValueError:
            self.image = images[self.direction][0]
        if image_index == 9:
            self.is_attacking = False
            if self.rect.colliderect(self.target.rect):
                self.hit(self.target)

    def damaged_animation(self) -> None:
        images = {'left': self.images_damaged_left, 'right': self.images_damaged_right}
        image_index = images[self.direction].index(self.image) + 1
        self.image = images[self.direction][image_index]
        if image_index == len(self.images_damaged_left) - 1:
            self.is_damaged = False

    def die_animation(self) -> None:
        images = {'left': self.images_died_left, 'right': self.images_died_left}
        try:
            image_index = images[self.direction].index(self.image) + 1
            self.image = images[self.direction][image_index]
            if image_index == len(self.images_died_left) - 1:
                self.kill()
        except ValueError:
            self.image = images[self.direction][0]

    def attack(self) -> None:
        """Switches hero mode to attack"""
        self.is_attacking = True
        if self.direction == 'right':
            self.image = ElectroEnemy.images_attacking_right[0]
        elif self.direction == 'left':
            self.image = ElectroEnemy.images_attacking_left[0]

    def update_image(self) -> None:
        if not self.is_died:
            if not self.is_damaged:
                if not self.is_attacking and not self.is_damaged:
                    if not self.is_running:
                        self.standing_animation()
                    else:
                        self.running_animation()
                    pygame.time.set_timer(settings.ELECTRO_ENEMY_EVENT_TYPE, 120)
                else:
                    self.attacking_animation()
                    pygame.time.set_timer(settings.ELECTRO_ENEMY_EVENT_TYPE, 75)
            else:
                self.damaged_animation()
        else:
            self.die_animation()


class ElectroEnemy(Enemy):
    images_standing_right = settings.ELECTRO_ENEMY_IMAGES["right_standing"]
    images_standing_left = [pygame.transform.flip(i, True, False) for i in images_standing_right]
    images_running_right = settings.ELECTRO_ENEMY_IMAGES["right_running"]
    images_running_left = [pygame.transform.flip(i, True, False) for i in images_running_right]
    images_attacking_right = settings.ELECTRO_ENEMY_IMAGES["right_attacking"]
    images_attacking_left = [pygame.transform.flip(i, True, False) for i in images_attacking_right]
    images_damaged_right = settings.ELECTRO_ENEMY_IMAGES["right_damaged"]
    images_damaged_left = [pygame.transform.flip(i, True, False) for i in images_damaged_right]
    images_died_right = settings.ELECTRO_ENEMY_IMAGES["right_die"]
    images_died_left = [pygame.transform.flip(i, True, False) for i in images_died_right]

    def __init__(self, position: typing.Tuple[int, int], target: Hero, *groups):
        super().__init__(position, target, *groups)

        self.damage = 5
        self.health = 50
