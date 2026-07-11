"""Game settings and tunable constants."""


class Settings:
    """Store all settings for Alien Invasion."""

    def __init__(self) -> None:
        """Initialize the game settings."""
        # Screen
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (230, 230, 230)

        # Ship
        self.ship_speed = 1.5

        # Bullets
        self.bullet_speed = 1.0
        self.bullet_height = 15
        self.bullet_width = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Aliens
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        self.alien_points = 50
