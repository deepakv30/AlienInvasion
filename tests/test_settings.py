"""Tests for the Settings class."""

from alien_invasion.settings import Settings


class TestSettings:
    def test_default_screen_size(self, settings):
        assert settings.screen_width == 1280
        assert settings.screen_height == 720

    def test_bg_color_is_rgb_tuple(self, settings):
        assert isinstance(settings.bg_color, tuple)
        assert len(settings.bg_color) == 3
        assert all(0 <= c <= 255 for c in settings.bg_color)

    def test_ship_speed_positive(self, settings):
        assert settings.ship_speed > 0

    def test_bullet_defaults(self, settings):
        assert settings.bullet_speed > 0
        assert settings.bullet_width > 0
        assert settings.bullet_height > 0
        assert settings.bullets_allowed >= 1
        assert isinstance(settings.bullet_color, tuple)
        assert len(settings.bullet_color) == 3

    def test_alien_defaults(self, settings):
        assert settings.alien_speed > 0
        assert settings.fleet_drop_speed > 0
        assert settings.fleet_direction in (1, -1)
        assert settings.alien_points > 0

    def test_independent_instances(self):
        a = Settings()
        b = Settings()
        a.ship_speed = 99
        assert b.ship_speed != 99
