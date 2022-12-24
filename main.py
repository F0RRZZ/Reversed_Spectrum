import pygame

from settings import *
from characters import *
from game import Game


def main():
    pygame.init()

    game = Game()

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    running = True
    while running:
        screen.fill(pygame.Color("black"))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == ALCHEMIST_EVENT_TYPE:
                game.update_alchemists_images()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not game.hero.attacking:
                    game.hero.attack_animation()
            if event.type == HERO_EVENT_TYPE:
                game.update_heros_image()
        game.update()
        game.draw_sprites(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
