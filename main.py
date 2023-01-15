import sys
import pygame
import game
import tools
import settings


pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.display.set_caption("Reversed Spectrum")
screen = pygame.display.set_mode((1900, 1000), pygame.FULLSCREEN)
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)


def terminate():
    """Terminates the program"""
    pygame.quit()
    sys.exit()


def menu():
    """Menu window"""
    pygame.mixer.music.load("sounds/menu/menu_music.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(loops=-1)

    cursor_sprite_group = pygame.sprite.Group()

    cursor_image = settings.CURSOR_IMAGE
    cursor = pygame.sprite.Sprite(cursor_sprite_group)
    cursor.image = cursor_image
    cursor.rect = cursor.image.get_rect()

    while True:
        screen.fill((0, 0, 0))
        screen.blit(settings.MENU_IMAGE, (0, 0))

        tools.create_button(screen, "Reversed Spectrum", "center", 50, 128)
        start_button = tools.create_button(screen, "Начать игру", "center", 600, 64)
        quit_button = tools.create_button(screen, "Выйти из игры", "center", 700, 64)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEMOTION:
                cursor.rect.topleft = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button[0][0] <= event.pos[0] <= start_button[1][0] and start_button[0][1] <= event.pos[1] <= \
                        start_button[1][1]:
                    settings.MENU_SOUNDS["hover"].play()
                    pygame.mixer.music.stop()
                    main()
                elif quit_button[0][0] <= event.pos[0] <= quit_button[1][0] and quit_button[0][1] <= event.pos[1] <= \
                        quit_button[1][1]:
                    terminate()
        cursor_sprite_group.draw(screen)
        pygame.display.flip()


def pause(screen: pygame.Surface, game: game.Game) -> None:
    """
    Pauses the game
    :param screen: pygame surface object
    :param game: game class object
    """
    cursor_sprite_group = pygame.sprite.Group()

    cursor_image = settings.CURSOR_IMAGE
    cursor = pygame.sprite.Sprite(cursor_sprite_group)
    cursor.image = cursor_image
    cursor.rect = cursor.image.get_rect()

    while True:
        for event in pygame.event.get():
            screen.fill((0, 0, 0))
            tools.create_button(screen, "Пауза", "center", 50, 128)
            continue_btn = tools.create_button(screen, "Продолжить игру", "center", 500, 64)
            exit_btn = tools.create_button(screen, "Выйти в главное меню", "center", 600, 64)
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


def main():
    game_obj = game.Game()

    running = True
    while running:
        screen.fill(pygame.Color("black"))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_obj.is_paused = not game_obj.is_paused
                if event.key == pygame.K_f and not game_obj.is_paused:
                    game_obj.hero_interaction()
                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5,
                                 pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                    game.inventory.get_features(event.key)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not game_obj.hero.is_attacking and not game_obj.is_paused:
                    game_obj.hero_attack()
            if event.type == settings.ALCHEMIST_EVENT_TYPE:
                game_obj.update_alchemists_images()
            if event.type == settings.HERO_IMAGE_UPDATE_EVENT_TYPE:
                game_obj.update_heros_image()
            if event.type == settings.HERO_STEP_SOUND_EVENT_TYPE:
                if game_obj.hero.is_walking and not game_obj.is_paused:
                    settings.HERO_SOUNDS["step"].play()
            if event.type == settings.ELECTRO_ENEMY_EVENT_TYPE:
                game_obj.update_electro_enemies_image()
            if event.type == settings.ELECTRO_ENEMY_MOVE_EVENT_TYPE:
                game_obj.move_enemies()
        game_obj.render(screen)
        if game_obj.is_paused:
            pause(screen, game_obj)
        pygame.display.flip()
        clock.tick(settings.FPS)

    terminate()


if __name__ == "__main__":
    menu()
