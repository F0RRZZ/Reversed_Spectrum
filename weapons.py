import pygame
import loaders
import typing


class Sword(pygame.sprite.Sprite):
    def __init__(self, position: typing.Tuple[int, int], image_scale: typing.Tuple[int, int], *groups):
        super().__init__(*groups)
        self.image = pygame.transform.scale(self.image, image_scale)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.type = "weapon"


class IronSword(Sword):
    image = loaders.load_image("iron sword.png")

    def __init__(self, position: typing.Tuple[int, int], image_scale: typing.Tuple[int, int], *groups):
        super().__init__(position, image_scale, *groups)
        self.damage = 10

    @staticmethod
    def give_self():
        return IronSword


class DiamondSword(Sword):
    image = loaders.load_image("diamond sword.png")

    def __init__(self, position: typing.Tuple[int, int], image_scale: typing.Tuple[int, int], *groups):
        super().__init__(position, image_scale, *groups)
        self.damage = 40

    @staticmethod
    def give_self():
        return DiamondSword
