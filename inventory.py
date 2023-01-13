import pygame
import weapons
import armor


class Inventory:
    def __init__(self):
        self.sprites = pygame.sprite.Group()
        self.weapon = weapons.IronSword((665, 1015), (50, 50), self.sprites)
        self.helmet = armor.IronHelmet((765, 1015), (50, 50), self.sprites)
        self.cuirass = armor.IronCuirass((845, 1015), (50, 50), self.sprites)
        self.gloves = armor.IronGloves((925, 1015), (50, 50), self.sprites)
        self.boots = armor.IronBoots((1005, 1015), (50, 50), self.sprites)
        self.artifacts = [None] * 4

    def change_weapon(self, weapon) -> None:
        self.weapon = weapon((665, 1015), (50, 50), self.sprites)

    def change_armor(self, new_armor, armor_type: str) -> None:
        match armor_type:
            case "helmet":
                self.helmet = new_armor((765, 1015), (50, 50), self.sprites)
            case "cuirass":
                self.cuirass = new_armor((845, 1015), (50, 50), self.sprites)
            case "gloves":
                self.gloves = new_armor((925, 1015), (50, 50), self.sprites)
            case "boots":
                self.boots = new_armor((1005, 1015), (50, 50), self.sprites)

    def get_defence_value(self) -> int:
        defence = self.helmet.defence + self.cuirass.defence + self.gloves.defence + self.boots.defence
        for item in self.artifacts:
            if item is not None:
                ...
        return defence / 100

    def get_attack_value(self) -> int:
        return self.weapon.damage if self.weapon is not None else 0

    def render(self, screen: pygame.Surface) -> None:
        """
            Renders inventory.
            :param screen: pygame surface object
            """
        x_pos = 650
        pygame.draw.rect(screen, pygame.Color("dark gray"), (x_pos, 1000, 80, 80), 0)
        pygame.draw.rect(screen, pygame.Color("black"), (x_pos, 1000, 80, 80), 3)
        x_pos += 100
        for i in range(8):
            pygame.draw.rect(screen, pygame.Color("dark gray"), (x_pos, 1000, 80, 80), 0)
            pygame.draw.rect(screen, pygame.Color("black"), (x_pos, 1000, 80, 80), 3)
            x_pos += 80 if i != 3 else 100
        self.sprites.draw(screen)
