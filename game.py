import os, sys

# Prohibit Pygame from polluting `/dev/stdout`.
import time

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg

mouse_cursor = pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND)
fuckenWeirdHand = pg.image.load("fucken-weird-hand.png")
fuckenWeirdHand_surface = pg.surface.Surface((81, 101))
fuckenWeirdHand_cursor = pg.Cursor((17, 89), fuckenWeirdHand_surface) # Tip of the forefinger is the hotspot.


def main():
    pg.init()
    pg.display.set_mode((800, 600))
    pg.mouse.set_cursor(mouse_cursor)

    fuckenWeirdHand_surface.convert_alpha()
    fuckenWeirdHand_surface.fill(color = pg.Color(0,0,0,255)) # Make the surface transparent, except where we actually draw
    pg.Surface.blit(fuckenWeirdHand_surface, fuckenWeirdHand, (0, 0))
    pg.mouse.set_cursor(fuckenWeirdHand_cursor)


    toQuit = False
    while not toQuit:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit(0) # Explicitly return zero when the game was closed cleanly.
