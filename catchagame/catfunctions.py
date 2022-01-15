import pygame as pg

pg.init()


# 140 by 140 size for tabs
# 1251 x val for tabs
def icon_formatter(name, x, y, size_x, size_y):
    icon = pg.image.load(name)
    scaled_icon = pg.transform.scale(icon, (size_x, size_y))
    rect = icon.get_rect()
    move_icon = rect.move(x, y)
    return [scaled_icon, move_icon]


def create_text(in_text, x, y, size):
    font = pg.font.Font('Pixel.ttf', size)
    text = font.render(in_text, True, (0, 0, 0))
    rect = text.get_rect()
    move_text = rect.move(x, y)
    return [text, move_text]


