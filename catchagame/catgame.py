import os
import pygame as pg
import catfunctions

pg.init()

background = pg.display.set_mode((1400, 700))
pg.display.set_caption("catcha")

width = background.get_width()
height = background.get_height()

color_light = (170, 170, 170)

# dark shade of the button
color_dark = (100, 100, 100)

base_level = 0

kibble_icon = catfunctions.icon_formatter("kibble_icon.png", 0, 0, 100, 100)
fish_icon = catfunctions.icon_formatter("fish_icon.png", 0, 100, 100, 100)
milk_icon = catfunctions.icon_formatter("milk_icon.png", 0, 200, 100, 100)

kibble_counter = catfunctions.create_text("0", 100, 40, 50)
fish_counter = catfunctions.create_text("0", 100, 130, 50)
milk_counter = catfunctions.create_text("0", 100, 240, 50)

breadcat_lvl = catfunctions.create_text(f"level: {base_level}", 900, 100, 20)
breadcat_name = catfunctions.create_text("breadcat", 900, 60, 30)
breadcat_upgrade = catfunctions.icon_formatter("upgrade_icon.png", 1100, 60, 80, 80)
upgrade_hover = catfunctions.icon_formatter("upgrade_icon.png", 1080, 40, 100, 100)

# tabs
cat_icon = catfunctions.icon_formatter("cat_icon.png", 1251, 0, 140, 140)
gacha_icon = catfunctions.icon_formatter("gacha_icon.png", 1251, 140, 140, 140)
upgrades_icon = catfunctions.icon_formatter("upgrade_icon.png", 1251, 300, 140, 140)
achievements_icon = catfunctions.icon_formatter("achievements_icon.png", 1251, 450, 140, 140)

breadcat_idle = catfunctions.icon_formatter("breadcat_idle.png", 750, 30, 140, 140)
cat_menu = False

button_test = catfunctions.icon_formatter("button_test.png", 950, 100, 200, 50)

background.fill((255, 255, 255))
pg.draw.lines(background, (0, 0, 0), True, [(700, 0), (700, 700)], 5)
pg.draw.lines(background, (0, 0, 0), True, [(1250, 0), (1250, 700)], 5)
pg.draw.lines(background, (0, 0, 0), True, [(1250, 139), (1400, 139)], 5)
pg.draw.lines(background, (0, 0, 0), True, [(1250, 289), (1400, 289)], 5)
pg.draw.lines(background, (0, 0, 0), True, [(1250, 439), (1400, 439)], 5)
pg.draw.lines(background, (0, 0, 0), True, [(1250, 589), (1400, 589)], 5)

background.blit(fish_icon[0], fish_icon[1])
background.blit(kibble_icon[0], kibble_icon[1])
background.blit(milk_icon[0], milk_icon[1])
background.blit(kibble_counter[0], kibble_counter[1])
background.blit(fish_counter[0], fish_counter[1])
background.blit(milk_counter[0], milk_counter[1])

background.blit(gacha_icon[0], gacha_icon[1])
background.blit(upgrades_icon[0], upgrades_icon[1])
background.blit(achievements_icon[0], achievements_icon[1])

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

        if event.type == pg.MOUSEBUTTONDOWN:
            if 1251 <= mouse[0] <= 1251 + 149 and 0 <= mouse[1] <= 139:
                catfunctions.box(background, 750, 50)
                # background.blit(button_test[0], button_test[1])
                if cat_menu:
                    cat_menu = False
                else:
                    cat_menu = True

    mouse = pg.mouse.get_pos()
    if 1251 <= mouse[0] <= 1251 + 149 and 0 <= mouse[1] <= 139:
        pg.draw.rect(background, color_dark, [1253, 0, 149, 137])

    else:
        pg.draw.rect(background, color_light, [1253, 0, 149, 137])

    if cat_menu:
        catfunctions.box(background, 750, 50)
        background.blit(breadcat_idle[0], breadcat_idle[1])
        background.blit(breadcat_name[0], breadcat_name[1])
        background.blit(breadcat_lvl[0], breadcat_lvl[1])
        background.blit(breadcat_upgrade[0], breadcat_upgrade[1])
        if 1100 <= mouse[0] <= 1100 + 100 and 60 <= mouse[1] <= 160:
            pg.draw.rect(background, (0, 0, 0), [1110, 65, 60, 70])
        else:
            pg.draw.rect(background, (255, 255, 255), [1110, 65, 60, 70])
            background.blit(breadcat_upgrade[0], breadcat_upgrade[1])
    else:
        pg.draw.rect(background, (255, 255, 255), [710, 5, 530, 690])

    background.blit(cat_icon[0], cat_icon[1])
    pg.display.update()
