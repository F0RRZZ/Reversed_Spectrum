import pygame

from image_loader import load_image

pygame.mixer.init()

FPS = 60

TILE_SIZE = (100, 100)
ALCHEMIST_SIZE = (100, 100)
ELECTRO_ENEMY_SIZE = (150, 150)

HERO_MOVE_SPEED = 10

HERO_IMAGE_UPDATE_EVENT_TYPE = 30
HERO_STEP_SOUND_EVENT_TYPE = 31
ALCHEMIST_EVENT_TYPE = 40
ELECTRO_ENEMY_EVENT_TYPE = 50
ELECTRO_ENEMY_MOVE_EVENT_TYPE = 51

MENU_IMAGE = pygame.transform.scale(load_image("menu_image.png"), (1920, 1080))
CURSOR_IMAGE = pygame.transform.scale(load_image("cursor.png"), (50, 50))

FREE_TYLES = ["small hell stone", "large hell stone", "grass"]

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

ELECTRO_ENEMY_IMAGES = {
    "right_standing": [pygame.transform.scale(load_image("elecenemy1.png"), (150, 150)),
                       pygame.transform.scale(load_image("elecenemy2.png"), (150, 150)),
                       pygame.transform.scale(load_image("elecenemy3.png"), (150, 150)),
                       pygame.transform.scale(load_image("elecenemy4.png"), (150, 150)),
                       pygame.transform.scale(load_image("elecenemy5.png"), (150, 150)),
                       pygame.transform.scale(load_image("elecenemy6.png"), (150, 150)),
                       pygame.transform.scale(load_image("elecenemy7.png"), (150, 150)),
                       pygame.transform.scale(load_image("elecenemy8.png"), (150, 150))],
    "right_running": [pygame.transform.scale(load_image("running_elecenemy1.png"), (150, 150)),
                      pygame.transform.scale(load_image("running_elecenemy2.png"), (150, 150)),
                      pygame.transform.scale(load_image("running_elecenemy3.png"), (150, 150)),
                      pygame.transform.scale(load_image("running_elecenemy4.png"), (150, 150)),
                      pygame.transform.scale(load_image("running_elecenemy5.png"), (150, 150)),
                      pygame.transform.scale(load_image("running_elecenemy6.png"), (150, 150))]
}

ALCHEMIST_IMAGES = {
    "right": [pygame.transform.scale(load_image("alchemist.png"), ALCHEMIST_SIZE),
              pygame.transform.scale(load_image("alchemist2.png"), ALCHEMIST_SIZE)]
}

MENU_SOUNDS = {"hover": pygame.mixer.Sound('sounds/menu/hover.wav')}
HERO_SOUNDS = {"step": pygame.mixer.Sound('sounds/hero/step.wav'),
               "attack1": pygame.mixer.Sound('sounds/hero/attack1.wav'),
               "attack2": pygame.mixer.Sound('sounds/hero/attack2.wav')}
