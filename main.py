import sys
import pygame

from settings import *
from characters import *
from errors import CoordinateError
from game import Game
from typing import Tuple


pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.display.set_caption("Reversed Spectrum")
screen = pygame.display.set_mode((1900, 1000))
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)


def terminate():
    pygame.quit()
    sys.exit()


def create_button(screen: pygame.Surface, text: str, x: int or str, y: int or str, font_size: int, text_color="white",
                  background="black") -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """Generates the buttons"""
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


def create_sprite(image: str, scale: Tuple[int, int], position: Tuple[int, int]) -> pygame.sprite.Sprite:
    """Creates sprites"""
    sprite = pygame.sprite.Sprite()
    sprite.image = pygame.transform.scale(load_image(image), scale)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x, sprite.rect.y = position
    return sprite


def menu():
    pygame.mixer.music.load("sounds/menu/menu_music.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(loops=-1)

    cursor_sprite_group = pygame.sprite.Group()

    cursor_image = CURSOR_IMAGE
    cursor = pygame.sprite.Sprite(cursor_sprite_group)
    cursor.image = cursor_image
    cursor.rect = cursor.image.get_rect()

    while True:
        screen.fill((0, 0, 0))
        screen.blit(MENU_IMAGE, (0, 0))

        create_button(screen, "Reversed Spectrum", "center", 50, 128)
        start_button = create_button(screen, "Начать игру", "center", 600, 64)
        quit_button = create_button(screen, "Выйти из игры", "center", 700, 64)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEMOTION:
                cursor.rect.topleft = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button[0][0] <= event.pos[0] <= start_button[1][0] and start_button[0][1] <= event.pos[1] <= \
                        start_button[1][1]:
                    MENU_SOUNDS["hover"].play()
                    pygame.mixer.music.stop()
                    main()
                elif quit_button[0][0] <= event.pos[0] <= quit_button[1][0] and quit_button[0][1] <= event.pos[1] <= \
                        quit_button[1][1]:
                    terminate()
        cursor_sprite_group.draw(screen)
        pygame.display.flip()


def pause(screen: pygame.Surface, game: Game):
    cursor_sprite_group = pygame.sprite.Group()

    cursor_image = CURSOR_IMAGE
    cursor = pygame.sprite.Sprite(cursor_sprite_group)
    cursor.image = cursor_image
    cursor.rect = cursor.image.get_rect()

    while True:
        for event in pygame.event.get():
            screen.fill((0, 0, 0))
            create_button(screen, "Пауза", "center", 50, 128)
            continue_btn = create_button(screen, "Продолжить игру", "center", 500, 64)
            exit_btn = create_button(screen, "Выйти в главное меню", "center", 600, 64)
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEMOTION:
                cursor.rect.topleft = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continue_btn[0][0] <= event.pos[0] <= continue_btn[1][0] and continue_btn[0][1] <= event.pos[1] <= \
                        continue_btn[1][1]:
                    game.is_paused = False
                    return
                elif exit_btn[0][0] <= event.pos[0] <= exit_btn[1][0] and exit_btn[0][1] <= event.pos[1] <= \
                        exit_btn[1][1]:
                    game.is_paused = False
                    menu()
        cursor_sprite_group.draw(screen)
        pygame.display.flip()


def draw_stats_bar(screen: pygame.Surface, health: int, mana: int) -> None:
    stats_group = pygame.sprite.Group()
    hurt = create_sprite("hurt.png", (50, 50), (10, 10))
    flask = create_sprite("mana.png", (60, 60), (5, 80))
    stats_group.add(hurt)
    stats_group.add(flask)
    pygame.draw.rect(screen, pygame.Color("black"), (80, 10, 400, 50), 0)
    pygame.draw.rect(screen, pygame.Color("red"), (85, 15, health * 4 - 10, 40), 0)
    pygame.draw.rect(screen, pygame.Color("black"), (80, 90, 400, 50), 0)
    pygame.draw.rect(screen, (47, 28, 255), (85, 95, mana * 4 - 10, 40), 0)
    stats_group.draw(screen)


def main():
    game = Game()

    running = True
    while running:
        screen.fill(pygame.Color("black"))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game.is_paused = not game.is_paused
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not game.hero.is_attacking and not game.is_paused:
                    game.hero_attack()
            if event.type == ALCHEMIST_EVENT_TYPE:
                game.update_alchemists_images()
            if event.type == HERO_IMAGE_UPDATE_EVENT_TYPE:
                game.update_heros_image()
            if event.type == HERO_STEP_SOUND_EVENT_TYPE:
                if game.hero.is_walking and not game.is_paused:
                    HERO_SOUNDS["step"].play()
            if event.type == ELECTRO_ENEMY_EVENT_TYPE:
                game.update_electro_enemies_image()
            if event.type == ELECTRO_ENEMY_MOVE_EVENT_TYPE:
                game.move_enemies()
        game.update()
        game.draw_sprites(screen)
        draw_stats_bar(screen, game.hero.health, game.hero.mana)
        if game.is_paused:
            pause(screen, game)
        pygame.display.flip()
        clock.tick(FPS)

    terminate()


if __name__ == "__main__":
    menu()
