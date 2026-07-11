"""Tests for the Ship class."""

from alien_invasion.sprites import Ship


class TestShip:
    def test_starts_at_bottom_center(self, game_context):
        ship = game_context.ship
        screen_rect = game_context.screen.get_rect()
        assert ship.rect.midbottom == screen_rect.midbottom

    def test_movement_flags_default_false(self, game_context):
        ship = game_context.ship
        assert ship.moving_right is False
        assert ship.moving_left is False

    def test_move_right(self, game_context):
        ship = game_context.ship
        start_x = ship.x
        ship.moving_right = True
        ship.update()
        assert ship.x == start_x + game_context.settings.ship_speed
        # rect.x is int; stay within 1px of the float position
        assert abs(ship.rect.x - ship.x) < 1

    def test_move_left(self, game_context):
        ship = game_context.ship
        start_x = ship.x
        ship.moving_left = True
        ship.update()
        assert ship.x == start_x - game_context.settings.ship_speed
        assert abs(ship.rect.x - ship.x) < 1

    def test_does_not_move_when_flags_false(self, game_context):
        ship = game_context.ship
        start_x = ship.x
        ship.update()
        assert ship.x == start_x

    def test_cannot_move_past_right_edge(self, game_context):
        ship = game_context.ship
        ship.rect.right = ship.screen_rect.right
        ship.x = float(ship.rect.x)
        ship.moving_right = True
        ship.update()
        assert ship.rect.right <= ship.screen_rect.right

    def test_cannot_move_past_left_edge(self, game_context):
        ship = game_context.ship
        ship.rect.left = 0
        ship.x = 0.0
        ship.moving_left = True
        ship.update()
        assert ship.rect.left >= 0
        assert ship.x == 0.0

    def test_blitme_does_not_raise(self, game_context):
        game_context.ship.blitme()

    def test_new_ship_uses_settings(self, game_context):
        ship = Ship(game_context)
        assert ship.settings is game_context.settings
