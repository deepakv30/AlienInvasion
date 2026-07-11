"""Tests for the Alien class."""

import pygame

from alien_invasion.sprites import Alien


class TestAlien:
    def test_starts_near_top_left(self, game_context):
        alien = Alien(game_context)
        assert alien.rect.x == alien.rect.width
        assert alien.rect.y == alien.rect.height
        assert alien.x == float(alien.rect.x)

    def test_update_moves_right_when_direction_positive(self, game_context):
        game_context.settings.fleet_direction = 1
        alien = Alien(game_context)
        start_x = alien.x
        alien.update()
        assert alien.x == start_x + game_context.settings.alien_speed
        assert abs(alien.rect.x - alien.x) < 1

    def test_update_moves_left_when_direction_negative(self, game_context):
        game_context.settings.fleet_direction = -1
        alien = Alien(game_context)
        start_x = alien.x
        alien.update()
        assert alien.x == start_x - game_context.settings.alien_speed

    def test_check_edges_false_when_in_center(self, game_context):
        alien = Alien(game_context)
        screen_rect = game_context.screen.get_rect()
        # Place clearly away from both edges
        alien.rect.x = screen_rect.width // 2
        assert not alien.check_edges()

    def test_check_edges_true_at_right_edge(self, game_context):
        alien = Alien(game_context)
        screen_rect = game_context.screen.get_rect()
        alien.rect.right = screen_rect.right
        assert alien.check_edges() is True

    def test_check_edges_true_at_left_edge(self, game_context):
        alien = Alien(game_context)
        alien.rect.left = 0
        assert alien.check_edges() is True

    def test_is_sprite(self, game_context):
        alien = Alien(game_context)
        assert isinstance(alien, pygame.sprite.Sprite)
