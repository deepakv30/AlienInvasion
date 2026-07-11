"""Tests for the Bullet class."""

import pygame

from bullet import Bullet


class TestBullet:
    def test_starts_at_ship_midtop(self, game_context):
        bullet = Bullet(game_context)
        assert bullet.rect.midtop == game_context.ship.rect.midtop

    def test_uses_settings_size_and_color(self, game_context):
        bullet = Bullet(game_context)
        assert bullet.rect.width == game_context.settings.bullet_width
        assert bullet.rect.height == game_context.settings.bullet_height
        assert bullet.color == game_context.settings.bullet_color

    def test_update_moves_upward(self, game_context):
        bullet = Bullet(game_context)
        start_y = bullet.y
        bullet.update()
        assert bullet.y == start_y - game_context.settings.bullet_speed
        assert abs(bullet.rect.y - bullet.y) < 1

    def test_multiple_updates_continue_upward(self, game_context):
        bullet = Bullet(game_context)
        start_y = bullet.y
        for _ in range(10):
            bullet.update()
        expected = start_y - 10 * game_context.settings.bullet_speed
        assert bullet.y == expected

    def test_draw_bullet_does_not_raise(self, game_context):
        bullet = Bullet(game_context)
        bullet.draw_bullet()

    def test_is_sprite(self, game_context):
        bullet = Bullet(game_context)
        assert isinstance(bullet, pygame.sprite.Sprite)
