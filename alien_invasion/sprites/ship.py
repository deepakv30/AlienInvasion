"""Player ship sprite."""

import pygame

from alien_invasion.paths import image_path


class Ship:
    """Manage the player's ship."""

    def __init__(self, ai_game) -> None:
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        self.image = pygame.image.load(image_path("ship.bmp"))
        self.rect = self.image.get_rect()

        # Start at bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Decimal horizontal position for smooth movement
        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def blitme(self) -> None:
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self) -> None:
        """Update the ship's position based on movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x
