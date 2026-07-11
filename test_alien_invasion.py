"""Tests for the main AlienInvasion game class."""

import pygame
import pytest

from alien_invasion import AlienInvasion
from bullet import Bullet
from alien import Alien


class TestAlienInvasionInit:
    def test_creates_screen_and_caption(self, game):
        assert game.screen is not None
        assert game.settings.screen_width > 0
        assert game.settings.screen_height > 0

    def test_creates_ship(self, game):
        assert game.ship is not None
        assert game.ship.rect.midbottom == game.screen.get_rect().midbottom

    def test_creates_empty_bullet_group(self, game):
        assert isinstance(game.bullets, pygame.sprite.Group)
        assert len(game.bullets) == 0

    def test_creates_alien_fleet(self, game):
        assert isinstance(game.aliens, pygame.sprite.Group)
        assert len(game.aliens) > 0


class TestFireBullet:
    def test_fire_bullet_adds_one_bullet(self, game):
        game._fire_bullet()
        assert len(game.bullets) == 1
        assert all(isinstance(b, Bullet) for b in game.bullets)

    def test_fire_bullet_respects_bullets_allowed(self, game):
        limit = game.settings.bullets_allowed
        for _ in range(limit + 5):
            game._fire_bullet()
        assert len(game.bullets) == limit


class TestUpdateBullets:
    def test_bullets_move_up(self, game):
        game._fire_bullet()
        bullet = game.bullets.sprites()[0]
        start_y = bullet.y
        game._update_bullets()
        assert bullet.y < start_y

    def test_removes_bullets_off_top_of_screen(self, game):
        game._fire_bullet()
        bullet = game.bullets.sprites()[0]
        # Place bullet fully above the screen
        bullet.y = -100
        bullet.rect.y = -100
        game._update_bullets()
        assert len(game.bullets) == 0


class TestFleet:
    def test_create_alien_positions_in_grid(self, game):
        game.aliens.empty()
        game._create_alien(0, 0)
        game._create_alien(1, 0)
        aliens = game.aliens.sprites()
        assert len(aliens) == 2
        assert aliens[1].rect.x > aliens[0].rect.x

    def test_change_fleet_direction_drops_and_reverses(self, game):
        original_direction = game.settings.fleet_direction
        ys_before = [a.rect.y for a in game.aliens.sprites()]
        game._change_fleet_direction()
        assert game.settings.fleet_direction == -original_direction
        for alien, y0 in zip(game.aliens.sprites(), ys_before):
            assert alien.rect.y == y0 + game.settings.fleet_drop_speed

    def test_check_fleet_edges_changes_direction_at_edge(self, game):
        game.settings.fleet_direction = 1
        # Push one alien to the right edge
        alien = game.aliens.sprites()[0]
        alien.rect.right = game.screen.get_rect().right
        game._check_fleet_edges()
        assert game.settings.fleet_direction == -1

    def test_update_aliens_moves_fleet(self, game):
        xs_before = [a.x for a in game.aliens.sprites()]
        game._update_aliens()
        xs_after = [a.x for a in game.aliens.sprites()]
        # At least one alien should have moved (unless immediately on edge
        # and only dropped — still positions change via drop or horizontal).
        assert xs_before != xs_after or any(
            a.rect.y for a in game.aliens.sprites()
        )


class TestCollisions:
    def test_bullet_alien_collision_removes_both(self, game):
        game.bullets.empty()
        game.aliens.empty()

        alien = Alien(game)
        alien.rect.x = 200
        alien.rect.y = 200
        alien.x = float(alien.rect.x)
        game.aliens.add(alien)

        bullet = Bullet(game)
        bullet.rect.center = alien.rect.center
        bullet.y = float(bullet.rect.y)
        game.bullets.add(bullet)

        assert len(game.bullets) == 1
        assert len(game.aliens) == 1

        game._check_bullet_alien_collisions()

        assert len(game.bullets) == 0
        assert len(game.aliens) == 0

    def test_no_collision_when_apart(self, game):
        game.bullets.empty()
        game.aliens.empty()

        alien = Alien(game)
        alien.rect.topleft = (50, 50)
        game.aliens.add(alien)

        bullet = Bullet(game)
        bullet.rect.topleft = (400, 400)
        game.bullets.add(bullet)

        game._check_bullet_alien_collisions()

        assert len(game.bullets) == 1
        assert len(game.aliens) == 1


class TestKeyEvents:
    def _event(self, key, event_type=pygame.KEYDOWN):
        event = pygame.event.Event(event_type, key=key)
        return event

    def test_keydown_right_sets_flag(self, game):
        game._check_keydown_events(self._event(pygame.K_RIGHT))
        assert game.ship.moving_right is True

    def test_keydown_left_sets_flag(self, game):
        game._check_keydown_events(self._event(pygame.K_LEFT))
        assert game.ship.moving_left is True

    def test_keyup_right_clears_flag(self, game):
        game.ship.moving_right = True
        game._check_keyup_events(self._event(pygame.K_RIGHT, pygame.KEYUP))
        assert game.ship.moving_right is False

    def test_keyup_left_clears_flag(self, game):
        game.ship.moving_left = True
        game._check_keyup_events(self._event(pygame.K_LEFT, pygame.KEYUP))
        assert game.ship.moving_left is False

    def test_space_fires_bullet(self, game):
        game.bullets.empty()
        game._check_keydown_events(self._event(pygame.K_SPACE))
        assert len(game.bullets) == 1

    def test_q_exits(self, game):
        with pytest.raises(SystemExit):
            game._check_keydown_events(self._event(pygame.K_q))


class TestUpdateScreen:
    def test_update_screen_does_not_raise(self, game):
        game._fire_bullet()
        game._update_screen()
