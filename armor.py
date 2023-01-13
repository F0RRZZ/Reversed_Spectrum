import pygame
import loaders
import typing


class Armor(pygame.sprite.Sprite):
    def __init__(self, position: typing.Tuple[int, int], image_scale: typing.Tuple[int, int], *groups):
        super().__init__(*groups)
        self.image = pygame.transform.scale(self.image, image_scale)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.type = "armor"


class IronHelmet(Armor):
    image = loaders.load_image("iron helmet.png")

    def __init__(self, position: typing.Tuple[int, int], image_scale: typing.Tuple[int, int], *groups):
        super().__init__(position, image_scale, *groups)
        self.armor_type = 'helmet'
        self.defence = 3

    @staticmethod
    def give_self():
        return IronHelmet


class DiamondHelmet(Armor):
    image = loaders.load_image("diamond helmet.png")

    def __init__(self, position: typing.Tuple[int, int], image_scale: typing.Tuple[int, int], *groups):
        super().__init__(position, image_scale, *groups)
        self.armor_type = 'helmet'
        self.defence = 10

    @staticmethod
    def give_self():
        return DiamondHelmet


class IronCuirass(Armor):
    image = loaders.load_image("iron cuirass.png")

    def __init__(self, position: typing.Tuple[int, int], image_scale: typing.Tuple[int, int], *groups):
        super().__init__(position, image_scale, *groups)
        self.armor_type = 'cuirass'
        self.defence = 5

    @staticmethod
    def give_self():
        return IronCuirass


class IronGloves(Armor):
    image = loaders.load_image("iron gloves.png")

    def __init__(self, position: typing.Tuple[int, int], image_scale: typing.Tuple[int, int], *groups):
        super().__init__(position, image_scale, *groups)
        self.armor_type = 'gloves'
        self.defence = 1

    @staticmethod
    def give_self():
        return IronGloves


class IronBoots(Armor):
    image = loaders.load_image("iron boots.png")

    def __init__(self, position: typing.Tuple[int, int], image_scale: typing.Tuple[int, int], *groups):
        super().__init__(position, image_scale, *groups)
        self.armor_type = 'boots'
        self.defence = 1

    @staticmethod
    def give_self():
        return IronBoots
