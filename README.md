# Alien Invasion 🚀

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)

A classic space shooter game built with **Python** and **Pygame**.

This project was developed as a hands-on learning exercise to practice object-oriented programming, game loops, collision detection, and event handling in Python.

## Features

- Player-controlled spaceship with movement and shooting
- Multiple enemy aliens that move and descend
- Collision detection between bullets and aliens
- Fleet edge detection and direction changes

## Requirements

- Python 3.8 or higher
- Pygame

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/deepakv30/AlienInvasion.git
   cd AlienInvasion
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Run the game:
   ```bash
   python -m alien_invasion
   ```

## Controls

| Key          | Action          |
|--------------|-----------------|
| Right Arrow  | Move ship right |
| Left Arrow   | Move ship left  |
| Spacebar     | Shoot bullet    |
| Q            | Quit the game   |

## Project Structure

```
AlienInvasion/
├── alien_invasion/           # Main game package
│   ├── __init__.py
│   ├── __main__.py           # python -m alien_invasion
│   ├── game.py               # Game loop and coordination
│   ├── settings.py           # Tunable settings
│   ├── paths.py              # Asset path helpers
│   ├── sprites/              # Sprite classes
│   │   ├── __init__.py
│   │   ├── ship.py
│   │   ├── alien.py
│   │   └── bullet.py
│   └── images/               # Game art assets
│       ├── ship.bmp
│       └── alien.bmp
├── tests/                    # Pytest suite
│   ├── conftest.py
│   ├── test_game.py
│   ├── test_settings.py
│   ├── test_ship.py
│   ├── test_alien.py
│   └── test_bullet.py
├── requirements.txt
├── pyproject.toml
├── LICENSE                    # MIT
├── SECURITY.md
└── README.md
```

## License

MIT License — see the [LICENSE](LICENSE) file for details.

## Security

See [SECURITY.md](SECURITY.md) for how to report vulnerabilities.

## Testing

```bash
pytest -v
```

Tests use pygame's dummy video driver and run without a display (including in CI).

## Disclaimer

This project was created **solely for learning and educational purposes**. It is based on concepts from the book *Python Crash Course* by Eric Matthes.

## Acknowledgments

- Inspired by *Python Crash Course* by Eric Matthes
- Built using the Pygame library

---

> Feel free to explore, modify, and use this project for learning game development with Python!
