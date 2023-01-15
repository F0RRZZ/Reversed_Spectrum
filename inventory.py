import pygame
import weapons
import armor


def draw_item_features(screen: pygame.Surface, item, artifact_multiplier=0) -> None:
    if item is None:
        return
    font = pygame.font.Font(None, 20)
    if item.type == "weapon":
        text = font.render(f"Att:+{item.damage} Mana:{item.mana}%", True, (255, 255, 255))
        screen.blit(text, (640, 985))
    elif item.type == "armor":
        start_pos = 740
        types = ["helmet", "cuirass", "gloves", "boots"]
        text = font.render(f"Def:+{item.defence}% Mana:{item.mana}%", True, (255, 255, 255))
        screen.blit(text, (start_pos + 80 * types.index(item.armor_type), 985))
    else:
        start_pos = 1080
        text = font.render(f"Def:+{item.defence}% Mana:{item.mana}%", True, (255, 255, 255))
        screen.blit(text, (start_pos + 80 * artifact_multiplier, 985))


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
        for i, artifact in enumerate(self.artifacts):
            if artifact is not None:
                if i.stats_checked:
                    draw_item_features(screen, artifact, i)
        self.sprites.draw(screen)

    def get_features(self, key):
        if key == pygame.K_1:
            self.weapon.stats_checked = not self.weapon.stats_checked
            self.helmet.stats_checked = False
            self.cuirass.stats_checked = False
            self.gloves.stats_checked = False
            self.boots.stats_checked = False
            for i in self.artifacts:
                if i is not None:
                    i.stats_checked = False
        elif key == pygame.K_2:
            self.helmet.stats_checked = not self.helmet.stats_checked
            self.weapon.stats_checked = False
            self.cuirass.stats_checked = False
            self.gloves.stats_checked = False
            self.boots.stats_checked = False
            for i in self.artifacts:
                if i is not None:
                    i.stats_checked = False
        elif key == pygame.K_3:
            self.cuirass.stats_checked = not self.cuirass.stats_checked
            self.weapon.stats_checked = False
            self.helmet.stats_checked = False
            self.gloves.stats_checked = False
            self.boots.stats_checked = False
            for i in self.artifacts:
                if i is not None:
                    i.stats_checked = False
        elif key == pygame.K_4:
            self.gloves.stats_checked = not self.gloves.stats_checked
            self.weapon.stats_checked = False
            self.helmet.stats_checked = False
            self.cuirass.stats_checked = False
            self.boots.stats_checked = False
            for i in self.artifacts:
                if i is not None:
                    i.stats_checked = False
        elif key == pygame.K_5:
            self.boots.stats_checked = not self.boots.stats_checked
            self.weapon.stats_checked = False
            self.helmet.stats_checked = False
            self.cuirass.stats_checked = False
            self.gloves.stats_checked = False
            for i in self.artifacts:
                if i is not None:
                    i.stats_checked = False
        elif key in [pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
            keys = [pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]
            self.weapon.stats_checked = False
            self.helmet.stats_checked = False
            self.cuirass.stats_checked = False
            self.gloves.stats_checked = False
            self.boots.stats_checked = False
            for i, artifact in enumerate(self.artifacts):
                if artifact is not None:
                    i.stats_checked = keys.index(key) == i
