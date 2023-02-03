import pygame
import weapons
import armor


def draw_item_features(screen: pygame.Surface, item) -> None:
    if item is None:
        return
    font = pygame.font.Font(None, 20)
    if item.type == "weapon":
        text = font.render(f"Att:+{item.damage} Mana:{item.mana}%", True, (255, 255, 255))
        screen.blit(text, (740, 985))
    elif item.type == "armor":
        start_pos = 840
        types = ["helmet", "cuirass", "gloves", "boots"]
        text = font.render(f"Def:+{item.defence}% Mana:{item.mana}%", True, (255, 255, 255))
        screen.blit(text, (start_pos + 80 * types.index(item.armor_type), 985))


class Inventory:
    def __init__(self):
        self.sprites = pygame.sprite.Group()
        self.weapon = weapons.IronSword((765, 1015), (50, 50), self.sprites)
        self.helmet = armor.IronHelmet((865, 1015), (50, 50), self.sprites)
        self.cuirass = armor.IronCuirass((945, 1015), (50, 50), self.sprites)
        self.gloves = armor.IronGloves((1025, 1015), (50, 50), self.sprites)
        self.boots = armor.IronBoots((1105, 1015), (50, 50), self.sprites)

    def change_weapon(self, weapon) -> None:
        self.weapon = weapon((765, 1015), (50, 50), self.sprites)

    def change_armor(self, new_armor, armor_type: str) -> None:
        if armor_type == "helmet":
            self.helmet = new_armor((865, 1015), (50, 50), self.sprites)
        elif armor_type == "cuirass":
            self.cuirass = new_armor((945, 1015), (50, 50), self.sprites)
        elif armor_type == "gloves":
            self.gloves = new_armor((1025, 1015), (50, 50), self.sprites)
        elif armor_type == "boots":
            self.boots = new_armor((1105, 1015), (50, 50), self.sprites)

    def get_defence_value(self) -> int:
        defence = self.helmet.defence + self.cuirass.defence + self.gloves.defence + self.boots.defence
        return defence / 100

    def get_attack_value(self) -> int:
        return self.weapon.damage if self.weapon is not None else 0

    def render(self, screen: pygame.Surface) -> None:
        """
            Renders inventory.
            :param screen: pygame surface object
            """
        x_pos = 750
        pygame.draw.rect(screen, pygame.Color("dark gray"), (x_pos, 1000, 80, 80), 0)
        pygame.draw.rect(screen, pygame.Color("black"), (x_pos, 1000, 80, 80), 3)
        x_pos += 100
        for i in range(4):
            pygame.draw.rect(screen, pygame.Color("dark gray"), (x_pos, 1000, 80, 80), 0)
            pygame.draw.rect(screen, pygame.Color("black"), (x_pos, 1000, 80, 80), 3)
            x_pos += 80 if i != 3 else 100
        if self.weapon.stats_checked:
            draw_item_features(screen, self.weapon)
        elif self.helmet.stats_checked:
            draw_item_features(screen, self.helmet)
        elif self.cuirass.stats_checked:
            draw_item_features(screen, self.cuirass)
        elif self.gloves.stats_checked:
            draw_item_features(screen, self.gloves)
        elif self.boots.stats_checked:
            draw_item_features(screen, self.boots)
        self.sprites.draw(screen)

    def get_features(self, key):
        if key == pygame.K_1:
            self.weapon.stats_checked = not self.weapon.stats_checked
            self.helmet.stats_checked = False
            self.cuirass.stats_checked = False
            self.gloves.stats_checked = False
            self.boots.stats_checked = False
        elif key == pygame.K_2:
            self.helmet.stats_checked = not self.helmet.stats_checked
            self.weapon.stats_checked = False
            self.cuirass.stats_checked = False
            self.gloves.stats_checked = False
            self.boots.stats_checked = False
        elif key == pygame.K_3:
            self.cuirass.stats_checked = not self.cuirass.stats_checked
            self.weapon.stats_checked = False
            self.helmet.stats_checked = False
            self.gloves.stats_checked = False
            self.boots.stats_checked = False
        elif key == pygame.K_4:
            self.gloves.stats_checked = not self.gloves.stats_checked
            self.weapon.stats_checked = False
            self.helmet.stats_checked = False
            self.cuirass.stats_checked = False
            self.boots.stats_checked = False
        elif key == pygame.K_5:
            self.boots.stats_checked = not self.boots.stats_checked
            self.weapon.stats_checked = False
            self.helmet.stats_checked = False
            self.cuirass.stats_checked = False
            self.gloves.stats_checked = False
