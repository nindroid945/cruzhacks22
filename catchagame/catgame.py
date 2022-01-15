import os
import pygame as pg
import catfunctions

pg.init()

background = pg.display.set_mode((1400, 700))
pg.display.set_caption("catcha")


def initialize():
    # currencies
    kibble_icon = catfunctions.icon_formatter("kibble_icon.png", 0, 0, 100, 100)
    fish_icon = catfunctions.icon_formatter("fish_icon.png", 0, 100, 100, 100)
    milk_icon = catfunctions.icon_formatter("milk_icon.png", 0, 200, 100, 100)

    kibble_counter = catfunctions.create_text("0", 100, 40, 50)
    fish_counter = catfunctions.create_text("0", 100, 130, 50)
    milk_counter = catfunctions.create_text("0", 100, 240, 50)

    # tabs
    cat_icon = catfunctions.icon_formatter("cat_icon.png", 1251, 0, 140, 140)
    gacha_icon = catfunctions.icon_formatter("gacha_icon.png", 1251, 140, 140, 140)
    upgrades_icon = catfunctions.icon_formatter("upgrade_icon.png", 1251, 300, 140, 140)
    achievements_icon = catfunctions.icon_formatter("achievements_icon.png", 1251, 450, 140, 140)

    background.fill((255, 255, 255))
    pg.draw.lines(background, (0, 0, 0), True, [(700, 0), (700, 700)], 3)
    pg.draw.lines(background, (0, 0, 0), True, [(1250, 0), (1250, 700)], 3)
    pg.draw.lines(background, (0, 0, 0), True, [(1250, 139), (1400, 139)], 3)
    pg.draw.lines(background, (0, 0, 0), True, [(1250, 289), (1400, 289)], 3)
    pg.draw.lines(background, (0, 0, 0), True, [(1250, 439), (1400, 439)], 3)
    pg.draw.lines(background, (0, 0, 0), True, [(1250, 589), (1400, 589)], 3)

    background.blit(fish_icon[0], fish_icon[1])
    background.blit(kibble_icon[0], kibble_icon[1])
    background.blit(milk_icon[0], milk_icon[1])
    background.blit(kibble_counter[0], kibble_counter[1])
    background.blit(fish_counter[0], fish_counter[1])
    background.blit(milk_counter[0], milk_counter[1])

    background.blit(cat_icon[0], cat_icon[1])
    background.blit(gacha_icon[0], gacha_icon[1])
    background.blit(upgrades_icon[0], upgrades_icon[1])
    background.blit(achievements_icon[0], achievements_icon[1])


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

        if event.type == pg.MOUSEBUTTONDOWN:
            pg.quit()

    initialize()
    pg.display.update()
