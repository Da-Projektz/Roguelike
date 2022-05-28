import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, rl_game):
        super().__init__()
        self.screen = rl_game.screen
        self.settings = rl_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = rl_game.player.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
