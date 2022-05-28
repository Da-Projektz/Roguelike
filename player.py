import pygame


class Player:

    def __init__(self, rl_game):
        self.screen = rl_game.screen
        self.settings = rl_game.settings

        self.screen_rect = rl_game.screen.get_rect()

        self.image = pygame.image.load('resources\images\main_guy.png')
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

        # positions
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.player_speed

        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.player_speed

        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.player_speed

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.player_speed

        # rect will only keep integer values
        # so we must first update self.x and self.y
        # then rect.x and rect.y

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
