import random

import pygame

from settings import *
from textures import *
from characters import *


def main():
    pygame.init()

    map_textures = pygame.sprite.Group()
    hero_group = pygame.sprite.Group()
    alchemists = pygame.sprite.Group()

    for y in range(13):
        for x in range(20):
            num = random.randint(0, 1)
            if num:
                LargeHellStoneTexture(map_textures, (100 * x, 100 * y))
            else:
                SmallHellStoneTexture(map_textures, (100 * x, 100 * y))
    hero = Hero(hero_group, (500, 500))
    alchemist = Alchemist(alchemists, (250, 250))

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    running = True
    while running:
        screen.fill(pygame.Color("grey"))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == ALCHEMIST_EVENT_TYPE:
                alchemist.update_image()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not hero.attacking:
                    hero.attack()
            if event.type == HERO_EVENT_TYPE:
                hero.update_image()
        hero.update_position()
        map_textures.draw(screen)
        alchemists.draw(screen)
        hero_group.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
