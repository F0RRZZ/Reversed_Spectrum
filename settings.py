import pygame
import pygame.mixer

from image_loader import load_image

TILE_IMAGES = {
    "grass": load_image("grass.png"),
    "stone": load_image("stone.png"),
    "large hell stone": load_image("hell_stone2.png"),
    "small hell stone": load_image("hell_stone3.png")
}

HERO_IMAGES = {
    "right_standing": [pygame.transform.scale(load_image("hero1.png"), (150, 150)),
                       pygame.transform.scale(load_image("hero2.png"), (150, 150)),
                       pygame.transform.scale(load_image("hero3.png"), (150, 150)),
                       pygame.transform.scale(load_image("hero2.png"), (150, 150)),
                       pygame.transform.scale(load_image("hero1.png"), (150, 150))],
    "right_walking": [pygame.transform.scale(load_image("walking_hero1.png"), (150, 150)),
                      pygame.transform.scale(load_image("walking_hero2.png"), (150, 150)),
                      pygame.transform.scale(load_image("walking_hero3.png"), (150, 150)),
                      pygame.transform.scale(load_image("walking_hero4.png"), (150, 150)),
                      pygame.transform.scale(load_image("walking_hero5.png"), (150, 150)),
                      pygame.transform.scale(load_image("walking_hero6.png"), (150, 150))],
    "right_attacking": [pygame.transform.scale(load_image("hero1.png"), (150, 150)),
                        pygame.transform.scale(load_image("attacking_hero1.png"), (150, 174)),
                        pygame.transform.scale(load_image("attacking_hero2.png"), (300, 156)),
                        pygame.transform.scale(load_image("attacking_hero3.png"), (150, 150)),
                        pygame.transform.scale(load_image("attacking_hero4.png"), (150, 150)),
                        pygame.transform.scale(load_image("attacking_hero5.png"), (150, 150))],
}

TILE_SIZE = (100, 100)

HERO_EVENT_TYPE = 30
ALCHEMIST_EVENT_TYPE = 40
