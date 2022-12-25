import sys
import pygame

from settings import *
from characters import *
from errors import CoordinateError
from game import Game

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.display.set_caption("Reversed Spectrum")
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()


def terminate():
    pygame.quit()
    sys.exit()


def create_button(screen: pygame.Surface, text: str, x, y, font_size: int, text_color="white",
                  background="black") -> tuple:
    font = pygame.font.Font(None, font_size)
    text_rendered = font.render(text, True, pygame.Color(text_color))
    text_rect = text_rendered.get_rect()
    if x != "center" and type(x) != int:
        raise CoordinateError('Координата может принимать только число или "center"')
    if y != "center" and type(y) != int:
        raise CoordinateError('Координата может принимать только число или "center"')
    text_rect.x = x if x != "center" else (1920 - text_rect.width) // 2
    text_rect.y = y if y != "center" else (1080 - text_rect.height) // 2
    pygame.draw.rect(screen, pygame.Color(background), ((text_rect.x - 10, text_rect.y - 10),
                                                        (text_rendered.get_width() + 20,
                                                         text_rendered.get_height() + 20)), 0)
    screen.blit(text_rendered, text_rect)
    return ((text_rect.x - 10, text_rect.y - 10),
            (text_rect.x + text_rendered.get_width() + 10,
             text_rect.y + text_rendered.get_height() + 10))


def menu():
    pygame.mixer.music.load("sounds/menu/menu_music.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(loops=-1)
    screen.blit(MENU_IMAGE, (0, 0))

    create_button(screen, "Reversed Spectrum", "center", 50, 128)
    start_button = create_button(screen, "Начать игру", "center", 600, 64)
    quit_button = create_button(screen, "Выйти из игры", "center", 700, 64)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button[0][0] <= event.pos[0] <= start_button[1][0] and start_button[0][1] <= event.pos[1] <= \
                        start_button[1][1]:
                    MENU_SOUNDS["hover"].play()
                    pygame.mixer.music.stop()
                    return
                elif quit_button[0][0] <= event.pos[0] <= quit_button[1][0] and quit_button[0][1] <= event.pos[1] <= \
                        quit_button[1][1]:
                    terminate()
        pygame.display.flip()
        clock.tick(FPS)


def main():
    game = Game()

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
                    game.hero.attack()
            if event.type == HERO_IMAGE_UPDATE_EVENT_TYPE:
                game.update_heros_image()
            if event.type == HERO_STEP_SOUND_EVENT_TYPE:
                if game.hero.walking:
                    HERO_SOUNDS["step"].play()
        game.update()
        game.draw_sprites(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    menu()
    main()
