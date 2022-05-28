import sys
import pygame
from pytmx.util_pygame import load_pygame

from settings import Settings
from player import Player
from bullet import Bullet
from tile import Tile


class RogueLike:

    def __init__(self, full_flag=True):
        pygame.init()
        self.settings = Settings()
        if full_flag == True:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height)
            )
            pygame.display.set_caption("Rogue Like")

        # TODO: For tileset
        # video mode must be set before this line
        # self.tmx_data = load_pygame('resources\\tilesets\\tmx\\terrain.tmx')

        #   for layer in tmx_data.visible_layers:
        #   print(layer)

        self.player = Player(self)
        self.bullets = pygame.sprite.Group()
        self.sprite_group = pygame.sprite.Group()

    def run_game(self):
        while True:
            self._check_events()
            self.player.update()
            self._update_bullets()
            # self._update_tiles()  # TODO: make this work some how.
            self._update_screen()

    def _update_tiles(self):
        for layer in self.tmx_data.visible_layers:
            if hasattr(layer, 'data'):
                for x, y, surf in layer.tiles():
                    pos = (x * 128, y * 128)
                    Tile(pos=pos, surf=surf, groups=self.sprite_group)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _check_events(self):
        for event in pygame.event.get():
            self._check_mouse_events(event)
            self._check_keydown_events(event)
            self._check_keyup_events(event)

    def _key_event_handler(self, event, key_down_flag):
        match event.key:
            case pygame.K_UP:
                self.player.moving_up = key_down_flag
            case pygame.K_DOWN:
                self.player.moving_down = key_down_flag
            case pygame.K_RIGHT:
                self.player.moving_right = key_down_flag
            case pygame.K_LEFT:
                self.player.moving_left = key_down_flag
            case pygame.K_q:  # if the q key is pressed quit.
                sys.exit()
            case pygame.K_SPACE:  # shoot gun key
                if key_down_flag:
                    self._fire_bullet()
            case _:
                print(f"key {event.key} not mapped")

    def _fire_bullet(self):
        if self.settings.bullets_allowed > len(self.bullets):
            print(f"n = {len(self.bullets)}")
            self.bullets.add(Bullet(self))

    def _check_keydown_events(self, event):
        if event.type == pygame.KEYDOWN:
            self._key_event_handler(event, True)

    def _check_keyup_events(self, event):
        if event.type == pygame.KEYUP:
            self._key_event_handler(event, False)

    def _check_mouse_events(self, event):
        if event.type == pygame.QUIT:
            sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.player.blitme()
        for bullet in self.bullets:
            bullet.draw_bullet()
        pygame.display.flip()


if __name__ == '__main__':
    rl = RogueLike(False)
    rl.run_game()
