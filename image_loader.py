import os
import pygame

from errors import ImageSearchError


def load_image(name, colorkey=None):
    fullname = os.path.join('images', name)
    if not os.path.isfile(fullname):
        raise ImageSearchError(f"Файл с изображением '{fullname}' не найден")
    image = pygame.image.load(fullname)
    return image
