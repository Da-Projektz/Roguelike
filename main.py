import game
from rich import print


# Using calver for now
VERSION = '220510.0-pre'

def main():
    print(f'Rouge-like game VERSION [bold red]{VERSION}[/bold red].')


# Protect other scripts from running main functions.
if __name__ == "__main__":
    main()
    game.main()
