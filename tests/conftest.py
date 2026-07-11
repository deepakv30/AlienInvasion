"""Shared pytest fixtures for Alien Invasion tests.

Uses the SDL dummy video driver so tests run headless (CI, SSH, no display).
"""

import os

# Must be set before pygame is imported by the game modules.
os.environ.setdefault("SDL_VIDEODRIVER", "dummy")

import pytest
import pygame

from alien_invasion import AlienInvasion
from alien_invasion.settings import Settings
from alien_invasion.sprites import Ship


@pytest.fixture(scope="session", autouse=True)
def _pygame_session():
    """Initialize pygame once per test session and tear it down at the end."""
    pygame.init()
    yield
    pygame.quit()


@pytest.fixture
def settings():
    """Fresh Settings instance for each test."""
    return Settings()


@pytest.fixture
def screen(settings):
    """A windowed pygame surface sized from Settings (not fullscreen)."""
    return pygame.display.set_mode(
        (settings.screen_width, settings.screen_height)
    )


@pytest.fixture
def game_context(settings, screen):
    """Minimal game-like object for unit-testing Ship, Bullet, and Alien.

    Provides the attributes those classes expect from AlienInvasion without
    constructing the full game (fleet, fullscreen, etc.).
    """

    class GameContext:
        pass

    ctx = GameContext()
    ctx.settings = settings
    ctx.screen = screen
    ctx.ship = Ship(ctx)
    ctx.bullets = pygame.sprite.Group()
    ctx.aliens = pygame.sprite.Group()
    return ctx


@pytest.fixture
def game(monkeypatch):
    """Fully constructed AlienInvasion instance in windowed mode.

    Patches set_mode so tests never open a real fullscreen display.
    """
    original_set_mode = pygame.display.set_mode

    def windowed_set_mode(*args, **kwargs):
        cfg = Settings()
        return original_set_mode((cfg.screen_width, cfg.screen_height))

    monkeypatch.setattr(pygame.display, "set_mode", windowed_set_mode)
    return AlienInvasion()
