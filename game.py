import os

# Prohibit Pygame from polluting `/dev/stdout`.
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg

dwarven_gauntlet = pg.image.load("dwarven_gauntlet.png")
dwarven_gauntlet_surface = pg.surface.Surface((28, 32))
dwarven_gauntlet_cursor = pg.Cursor((2, 0), dwarven_gauntlet_surface) # Tip of the forefinger is the hotspot.


def main():
    pg.init()
    pg.display.set_mode((800, 600))

    dwarven_gauntlet_surface.convert_alpha()
    # FIXME: and TODO: how does alpha work?
    # dwarven_gauntlet_surface.fill(color=pg.Color(0, 0, 0, 255)) # Make the surface transparent, except where we actually draw
    pg.Surface.blit(dwarven_gauntlet_surface, dwarven_gauntlet, (0, 0))
    pg.mouse.set_cursor(dwarven_gauntlet_cursor)

    to_quit = False
    while not to_quit:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                to_quit = True
                pg.quit()
                exit(0) # Explicitly return zero when the game was closed cleanly.
