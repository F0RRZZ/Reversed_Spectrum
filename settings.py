import pygame

from image_loader import load_image


TILE_IMAGES = {
    "grass": load_image("grass.png"),
    "stone": load_image("stone.png"),
    "large hell stone": load_image("hell_stone2.png"),
    "small hell stone": load_image("hell_stone3.png")
}

HERO_EVENT_TYPE = 30
ALCHEMIST_EVENT_TYPE = 40
