import os
import pygame as pg
import random
import catfunctions
import player
import icons


pg.init()
p = player.Player()

background = pg.display.set_mode((1400, 700))
pg.display.set_caption("catcha")

width = background.get_width()
height = background.get_height()

# colors
color_light = (170, 170, 170)
color_dark = (100, 100, 100)
vanilla = (242, 230, 177)

base_level = 0

kibble_counter = catfunctions.create_text(str(p.kibble), 100, 40, 50)
fish_counter = catfunctions.create_text(str(p.fish), 100, 130, 50)
milk_counter = catfunctions.create_text(str(p.milk), 100, 240, 50)


def update_kibble():
    pg.draw.rect(background, (255, 255, 255), [100, 0, 598, 100])
    kc = catfunctions.create_text(str(p.kibble), 100, 40, 50)
    background.blit(kc[0], kc[1])


class CatBox:
    def __init__(self, pp, name, y):
        self.pp = pp
        self.name = name
        self.y = y
        self.cat_idle = catfunctions.icon_formatter(pp.cats[name].icon, 750, y - 20, 140, 140)
        self.cat_name = catfunctions.create_text(name, 900, y + 10, 30)
        self.cat_lvl = catfunctions.create_text("level: {}".format(pp.cats[name].level), 900, y + 45, 20)
        self.cat_cost = catfunctions.create_text("cost: {} kibble".format(pp.cats[name].cost), 900, y + 70, 20)
        self.cat_upgrade1 = catfunctions.icon_formatter("upgrade_icon.png", 1100, y + 10, 80, 80)
        self.cat_upgrade2 = catfunctions.icon_formatter("upgrade_icon.png", 1105, y + 15, 70, 70)

    def display_cat_box(self):
        background.blit(self.cat_idle[0], self.cat_idle[1])
        background.blit(self.cat_name[0], self.cat_name[1])
        background.blit(self.cat_lvl[0], self.cat_lvl[1])
        background.blit(self.cat_upgrade1[0], self.cat_upgrade1[1])

    def hover_cat_box(self):
        pg.draw.rect(background, (255, 255, 255), [1110, self.y + 15, 60, 70])
        background.blit(self.cat_upgrade2[0], self.cat_upgrade2[1])
        background.blit(self.cat_cost[0], self.cat_cost[1])

    def unhover_cat_box(self):
        pg.draw.rect(background, (255, 255, 255), [1110, self.y + 15, 60, 70])
        background.blit(self.cat_upgrade1[0], self.cat_upgrade1[1])


cat_menu = False
gacha_menu = False
upgrade_menu = False
achievements_menu = False

button_test = catfunctions.icon_formatter("button_test.png", 950, 100, 200, 50)

background.fill((255, 255, 255))
pg.draw.rect(background, color_light, [1253, 0, 149, 700])
pg.draw.lines(background, (0, 0, 0), True, [(700, 0), (700, 700)], 5)
pg.draw.lines(background, (0, 0, 0), True, [(1250, 0), (1250, 700)], 5)
pg.draw.lines(background, (0, 0, 0), True, [(1250, 139), (1400, 139)], 5)
pg.draw.lines(background, (0, 0, 0), True, [(1250, 289), (1400, 289)], 5)
pg.draw.lines(background, (0, 0, 0), True, [(1250, 439), (1400, 439)], 5)
pg.draw.lines(background, (0, 0, 0), True, [(1250, 589), (1400, 589)], 5)

background.blit(icons.fish_icon[0], icons.fish_icon[1])
background.blit(icons.kibble_icon[0], icons.kibble_icon[1])
background.blit(icons.milk_icon[0], icons.milk_icon[1])

background.blit(kibble_counter[0], kibble_counter[1])
background.blit(fish_counter[0], fish_counter[1])
background.blit(milk_counter[0], milk_counter[1])

background.blit(icons.gacha_icon[0], icons.gacha_icon[1])
background.blit(icons.upgrades_icon[0], icons.upgrades_icon[1])
background.blit(icons.achievements_icon[0], icons.achievements_icon[1])

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.MOUSEBUTTONDOWN:
            # click counter
            if 0 <= mouse[0] <= 700 and 0 <= mouse[1] <= 700:
                p.kibble += p.kpc
                p.fish += p.fpc
                pg.draw.rect(background, (255, 255, 255), [100, 0, 598, 100])
                kibble_counter = catfunctions.create_text(str(p.kibble), 100, 40, 50)
                background.blit(kibble_counter[0], kibble_counter[1])
            if 1251 <= mouse[0] <= 1400:
                # cat
                if 0 <= mouse[1] <= 139:
                    # catfunctions.box(background, 750, 50)
                    # background.blit(button_test[0], button_test[1])
                    cat_menu = not cat_menu
                    gacha_menu, upgrade_menu, achievements_menu = [False, False, False]
                # gacha
                if 139 < mouse[1] <= 289:
                    gacha_menu = not gacha_menu
                    cat_menu, upgrade_menu, achievements_menu = [False, False, False]
                # upgrade
                if 289 < mouse[1] <= 439:
                    upgrade_menu = not upgrade_menu
                    cat_menu, gacha_menu, achievements_menu = [False, False, False]
                # achievement
                if 439 < mouse[1] <= 589:
                    achievements_menu = not achievements_menu
                    cat_menu, gacha_menu, upgrade_menu = [False, False, False]
                # exit
                # if 589 < mouse[1] <= 700:
            if cat_menu:
                if "breadcat" in p.cats:
                    if 1100 <= mouse[0] <= 1200 and 60 <= mouse[1] <= 160:
                        if p.kibble >= 10:
                            #base_level += 1
                            #p.cats["breadcat"].level += 1
                            p.cats["breadcat"].levelup()
                            p.kpc += 1
                            p.kibble -= 10
                            update_kibble()
                if "dogcat" in p.cats:
                    if 1100 <= mouse[0] <= 1200 and 210 <= mouse[1] <= 310:
                        if p.kibble >= 10:
                            p.cats["dogcat"].levelup()
                            p.kpc += 1
                            p.kibble -= 10
                            update_kibble()

            if gacha_menu:
                if 750 <= mouse[0] <= 1200 and 250 <= mouse[1] <= 350:
                    if p.kibble >= 10:
                        rolls = [("breadcat", "breadcat_idle.png", 10), ("dogcat", "dogcat_idle.png", 10)]
                        i = random.randint(0, 1)
                        p.get_cat(rolls[i][0], rolls[i][1], rolls[i][2])
                        p.kibble -= 10
                        update_kibble()

    # hover
    mouse = pg.mouse.get_pos()
    if 1251 <= mouse[0] <= 1400:
        # cat
        if 0 <= mouse[1] <= 139:
            pg.draw.rect(background, color_dark, [1253, 0, 149, 137])
        else:
            pg.draw.rect(background, color_light, [1253, 0, 149, 137])
        # gacha
        if 139 < mouse[1] <= 289:
            pg.draw.rect(background, color_dark, [1253, 141, 149, 146])
        else:
            pg.draw.rect(background, color_light, [1253, 141, 149, 146])
        # upgrade
        if 289 < mouse[1] <= 439:
            pg.draw.rect(background, color_dark, [1253, 291, 149, 146])
        else:
            pg.draw.rect(background, color_light, [1253, 291, 149, 146])
        # achievement
        if 439 < mouse[1] <= 589:
            pg.draw.rect(background, color_dark, [1253, 441, 149, 146])
        else:
            pg.draw.rect(background, color_light, [1253, 441, 149, 146])
        # exit
        if 589 < mouse[1] <= 700:
            pg.draw.rect(background, color_dark, [1253, 591, 149, 109])
        else:
            pg.draw.rect(background, color_light, [1253, 591, 149, 109])
    else:
        pg.draw.rect(background, color_light, [1253, 0, 149, 137])
        pg.draw.rect(background, color_light, [1253, 141, 149, 146])
        pg.draw.rect(background, color_light, [1253, 291, 149, 146])
        pg.draw.rect(background, color_light, [1253, 441, 149, 146])
        pg.draw.rect(background, color_light, [1253, 591, 149, 109])

    """
    if 1251 <= mouse[0] <= 1400 and 0 <= mouse[1] <= 139:
        pg.draw.rect(background, color_dark, [1253, 0, 149, 137])
    elif 1251 <= mouse[0] <= 1400 and 139 <= mouse[1] <= 289:
        pg.draw.rect(background, color_dark, [1253, 141, 149, 139])
    else:
        pg.draw.rect(background, color_light, [1253, 0, 149, 137])
    """
    if cat_menu:
        pg.draw.rect(background, [255, 255, 255], [702, 0, 546, 700])
        catfunctions.box(background, 750, 50)
        catfunctions.box(background, 750, 200)
        catfunctions.box(background, 750, 350)
        catfunctions.box(background, 750, 500)
        if "breadcat" in p.cats:
            c = CatBox(p, "breadcat", 50)
            c.display_cat_box()
            if 1100 <= mouse[0] <= 1200 and 60 <= mouse[1] <= 160:
                c.hover_cat_box()
            else:
                c.unhover_cat_box()
        else:
            locked = catfunctions.create_text("locked cat", 900, 60, 30)
            background.blit(locked[0], locked[1])
        if "dogcat" in p.cats:
            cat_idle = catfunctions.icon_formatter(p.cats["dogcat"].icon, 750, 180, 140, 140)
            cat_name = catfunctions.create_text("dogcat", 900, 210, 30)
            cat_lvl = catfunctions.create_text("level: {}".format(p.cats["dogcat"].level), 900, 245, 20)
            cat_cost = catfunctions.create_text("cost: {} kibble".format(p.cats["dogcat"].cost), 900, 270, 20)
            cat_upgrade1 = catfunctions.icon_formatter("upgrade_icon.png", 1100, 210, 80, 80)
            cat_upgrade2 = catfunctions.icon_formatter("upgrade_icon.png", 1105, 215, 70, 70)
            background.blit(cat_idle[0], cat_idle[1])
            background.blit(cat_name[0], cat_name[1])
            background.blit(cat_lvl[0], cat_lvl[1])
            background.blit(cat_upgrade1[0], cat_upgrade1[1])
            if 1100 <= mouse[0] <= 1200 and 210 <= mouse[1] <= 310:
                pg.draw.rect(background, (255, 255, 255), [1110, 215, 60, 70])
                background.blit(cat_upgrade2[0], cat_upgrade2[1])
                background.blit(cat_cost[0], cat_cost[1])
            else:
                pg.draw.rect(background, (255, 255, 255), [1110, 215, 60, 70])
                background.blit(cat_upgrade1[0], cat_upgrade1[1])
        else:
            locked = catfunctions.create_text("locked cat", 900, 210, 30)
            background.blit(locked[0], locked[1])
    elif gacha_menu:
        pg.draw.rect(background, (255, 255, 255), [702, 0, 546, 700])
        catfunctions.box(background, 750, 250)
        catfunctions.box(background, 750, 400)
        kibble_gacha = catfunctions.create_text("kibble gacha", 760, 285, 30)
        fish_gacha = catfunctions.create_text("fish gacha", 760, 435, 30)
        background.blit(kibble_gacha[0], kibble_gacha[1])
        background.blit(fish_gacha[0], fish_gacha[1])
    elif upgrade_menu:
        pg.draw.rect(background, (255, 255, 255), [702, 0, 546, 700])
        catfunctions.box(background, 750, 50)
        catfunctions.box(background, 750, 200)
        catfunctions.box(background, 750, 350)
        catfunctions.box(background, 750, 500)
        upgrade_name = catfunctions.create_text("mega kibbler", 760, 60, 30)
        upgrade_level = catfunctions.create_text("level: {}".format(p.upgrades["mega kibbler"]), 760, 95, 20)
        upgrade_cost = catfunctions.create_text("cost: {} fish".format(10), 760, 120, 20)
        upgrade_upgrade1 = catfunctions.icon_formatter("upgrade_icon.png", 1100, 60, 80, 80)
        upgrade_upgrade2 = catfunctions.icon_formatter("upgrade_icon.png", 1105, 65, 70, 70)
        background.blit(upgrade_name[0], upgrade_name[1])
        background.blit(upgrade_level[0], upgrade_level[1])
        background.blit(upgrade_cost[0], upgrade_cost[1])
        background.blit(upgrade_upgrade1[0], upgrade_upgrade1[1])
        if 1100 <= mouse[0] <= 1200 and 60 <= mouse[1] <= 160:
            pg.draw.rect(background, (255, 255, 255), [1110, 65, 60, 70])
            background.blit(upgrade_upgrade2[0], upgrade_upgrade2[1])
            background.blit(upgrade_cost[0], upgrade_cost[1])
        else:
            pg.draw.rect(background, (255, 255, 255), [1110, 65, 60, 70])
            background.blit(upgrade_upgrade1[0], upgrade_upgrade1[1])
    else:
        pg.draw.rect(background, (255, 255, 255), [702, 0, 546, 700])

    background.blit(icons.cat_icon[0], icons.cat_icon[1])
    background.blit(icons.gacha_icon[0], icons.gacha_icon[1])
    background.blit(icons.upgrades_icon[0], icons.upgrades_icon[1])
    background.blit(icons.achievements_icon[0], icons.achievements_icon[1])
    background.blit(icons.exit_icon[0], icons.exit_icon[1])
    pg.display.update()