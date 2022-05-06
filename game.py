import os, sys

# Prohibit Pygame from polluting `/dev/stdout`.
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg


def main():
    pg.init()
