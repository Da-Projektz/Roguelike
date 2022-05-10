import os

# Prohibit Pygame from polluting `/dev/stdout`.
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg

dwarven_gauntlet = pg.image.load("dwarven_gauntlet.png")
dwarven_gauntlet_surface = pg.surface.Surface((28, 32), pg.SRCALPHA)
dwarven_gauntlet_cursor = pg.Cursor((2, 0), dwarven_gauntlet_surface) # Tip of the forefinger is the hotspot.


def main():
    pg.init()
    pg.display.set_mode((800, 600))

    dwarven_gauntlet.convert_alpha()
    dwarven_gauntlet_surface.convert_alpha()
    pg.Surface.blit(dwarven_gauntlet_surface, dwarven_gauntlet, (0, 0))
    pg.mouse.set_cursor(dwarven_gauntlet_cursor)

    to_quit = False
    while not to_quit:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                to_quit = True
                pg.quit()
