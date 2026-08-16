# Snake Game
## Description

A terminal/GUI-based Snake game built in Python with login, leaderboardls features.

## Controls

- Arrow keys: Move the snake
- P: Pause the game
- R: Restart the game
- Q: Quit the game

## Requirements

- Python 3.8 or later
- Pygame
- A terminal or GUI environment

## Setup
1. Create a Virtual Environment
```bash
python3 -m venv .venv
```

2. Activate the Virtual Environment

On macOS/Linux:
```bash
source .venv/bin/activate
```

On Windows:
```bash
.venv\Scripts\activate
```

3. Install Pygame

Make sure the virtual environment is activated, then install Pygame:

```bash
python -m pip install pygame
```

Verify that Pygame was installed correctly:

```bash
python -c "import pygame; print(pygame.version.ver)"
```

If the command prints a version number, Pygame is installed successfully.

4. Run the Game
```bash
python main.py
```

## Features

- User login and registration
- Snake gameplay using Pygame
- Score tracking
- Leaderboard