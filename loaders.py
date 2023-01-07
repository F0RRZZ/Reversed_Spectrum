import os
import pygame
import json
import exceptions
import tile


def load_image(name, colorkey=None):
    fullname = os.path.join('images', name)
    if not os.path.isfile(fullname):
        raise exceptions.ImageSearchError(f"Файл с изображением '{fullname}' не найден")
    image = pygame.image.load(fullname)
    return image


def load_map(level: int, all_sprites: pygame.sprite.Group, tiles_group: pygame.sprite.Group) -> list:
    tiles_arr = []
    with open(file=f'maps/level{level}.txt', mode='r', encoding="utf-8") as scheme:
        default = scheme.readline()[0]
        tiles = [i.split() for i in scheme.readlines()]
        with open(file="maps/tiles_ids.json", mode='r', encoding="utf-8") as ids:
            tiles_ids = json.load(ids)
            for row in range(1, len(tiles)):
                temp = []
                for t in range(len(tiles[row])):
                    t = tile.Tile(tiles_ids[tiles[row][t]], 100 * t, 100 * row, (100, 100), all_sprites, tiles_group)
                    temp.append(t)
                tiles_arr.append(temp)
    return tiles_arr
