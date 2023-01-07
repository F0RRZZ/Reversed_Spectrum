import pygame
import loaders
import exceptions
import typing


def create_sprite(image_name: str, scale: typing.Tuple[int, int],
                  position: typing.Tuple[int, int]) -> pygame.sprite.Sprite:
    """
    Creates sprites.
    :param image_name: image name
    :param scale: image size
    :param position: image position
    """
    sprite = pygame.sprite.Sprite()
    sprite.image = pygame.transform.scale(loaders.load_image(image_name), scale)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x, sprite.rect.y = position
    return sprite


def create_button(screen: pygame.Surface, text: str, x: typing.Union[int, str], y: typing.Union[int, str],
                  font_size: int,
                  text_color="white", background="black") -> typing.Tuple[typing.Tuple[int, int], typing.Tuple[int, int]]:
    """
    Generates the buttons.
    :param screen: pygame surface object
    :param text: Text in button.
    :param x: x_position
    :param y: y_position
    :param font_size: font_size(px)
    :param text_color: the color of the text in the button
    :param background: button background color
    """
    font = pygame.font.Font(None, font_size)
    text_rendered = font.render(text, True, pygame.Color(text_color))
    text_rect = text_rendered.get_rect()
    if x != "center" and type(x) != int:
        raise exceptions.CoordinateError('Координата может принимать только число или "center"')
    if y != "center" and type(y) != int:
        raise exceptions.CoordinateError('Координата может принимать только число или "center"')
    text_rect.x = x if x != "center" else (1920 - text_rect.width) // 2
    text_rect.y = y if y != "center" else (1080 - text_rect.height) // 2
    pygame.draw.rect(screen, pygame.Color(background), ((text_rect.x - 10, text_rect.y - 10),
                                                        (text_rendered.get_width() + 20,
                                                         text_rendered.get_height() + 20)), 0)
    screen.blit(text_rendered, text_rect)
    return ((text_rect.x - 10, text_rect.y - 10),
            (text_rect.x + text_rendered.get_width() + 10,
             text_rect.y + text_rendered.get_height() + 10))


def stats_drawer(screen: pygame.Surface, health: int, mana: int) -> None:
    """
    Renders heros stats.
    :param screen: pygame surface object
    :param health: health points
    :param mana: mana points
    """
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
