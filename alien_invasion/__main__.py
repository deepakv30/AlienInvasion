"""Entry point: ``python -m alien_invasion``."""

from alien_invasion.game import AlienInvasion


def main() -> None:
    game = AlienInvasion()
    game.run_game()


if __name__ == "__main__":
    main()
