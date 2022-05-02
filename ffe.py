import tcod
import os.path
from settings import Settings


class FallingForEternity:
    """Main class for assets and behavior"""

    def __init__(self):
        """initialize the game create resources"""

        self.settings = Settings()
        # Load the font, a 32 by 8 tile font with libtcod's old character layout.
        self.tileset = tcod.tileset.load_tilesheet(
            os.path.abspath("resources/images/dejavu10x10_gs_tc.png"),
            32, 8,
            tcod.tileset.CHARMAP_TCOD
        )

        # Create the main console.
        self.console = tcod.Console(
            self.settings.screen_width, self.settings.screen_width, order="F"
        )

    def run_game(self) -> None:
        """main game loop"""

        # Create a window based on this console and tileset.
        with tcod.context.new(  # New window for a console of size columns×rows.
            columns=self.console.width, rows=self.console.height, tileset=self.tileset,
        ) as context:
            while True:  # Main loop, runs until SystemExit is raised.
                self.console.clear()
                self.console.print(x=0, y=0, string=self.settings.game_name)
                context.present(self.console)  # Show the console.

                # This event loop will wait until at least one event is processed before exiting.
                # For a non-blocking event loop replace `tcod.event.wait` with `tcod.event.get`.
                for event in tcod.event.wait():
                    # Sets tile coordinates for mouse events.
                    context.convert_event(event)
                    print(event)  # Print event names and attributes.
                    if isinstance(event, tcod.event.Quit):
                        raise SystemExit()
            # The window will be closed after the above with-block exits.


if __name__ == "__main__":
    ffe = FallingForEternity()
    ffe.run_game()
