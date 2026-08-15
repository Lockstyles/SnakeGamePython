import pygame
import sys

from auth import auth_prompt
from leaderboard import display_leaderboard
from helpers import load_json, save_json
from core.game import SnakeGame, WIDTH, HEIGHT

SCORES_FILE = "data/scores.json"


def save_score(username, score):
    scores = load_json(SCORES_FILE, {})

    if username not in scores:
        scores[username] = {"high_score": score}
    elif score > scores[username]["high_score"]:
        scores[username]["high_score"] = score

    save_json(SCORES_FILE, scores)

def show_pause_menu(screen):
    font = pygame.font.SysFont(None, 36)
    text = font.render("PAUSED - Press P to resume", True, (255, 255, 255))
    screen.blit(text, (50, 200))


def main():
    username = auth_prompt()

    if username is None:
        print("Authentication failed. Exiting game.")
        return

    print(f"Welcome, {username}!")

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()

    game = SnakeGame(screen)
    paused = False

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_p:
                    paused = not paused

                elif event.key == pygame.K_UP and not paused:
                    game.change_direction((0, -1))

                elif event.key == pygame.K_DOWN and not paused:
                    game.change_direction((0, 1))

                elif event.key == pygame.K_LEFT and not paused:
                    game.change_direction((-1, 0))

                elif event.key == pygame.K_RIGHT and not paused:
                    game.change_direction((1, 0))

                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        if not paused:
            game.update()

        game.draw()

        if paused:
            show_pause_menu(screen)

        pygame.display.flip()
        clock.tick(game.speed)

        if game.game_over:
            print(f"\nGame Over! Final score: {game.score}")

            save_score(username, game.score)

            display_leaderboard()

            choice = input("\nPlay again? (y/n): ").lower()

            if choice == "y":
                game.reset()
                paused = False
            else:
                pygame.quit()
                sys.exit()



if __name__ == "__main__":
    main()
