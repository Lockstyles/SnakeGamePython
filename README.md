Snake Game
Description

A terminal/GUI-based Snake game built in Python with login, profile, leaderboard and settings features.

Setup
1. Create a Virtual Environment
python3 -m venv .venv

2. Activate the Virtual Environment

On macOS/Linux:

source .venv/bin/activate


On Windows:

.venv\Scripts\activate

3. Install Pygame

Make sure the virtual environment is activated, then install Pygame:

python -m pip install pygame


Verify that Pygame was installed correctly:

python -c "import pygame; print(pygame.version.ver)"


If the command prints a version number, Pygame is installed successfully.

4. Run the Game
python main.py

