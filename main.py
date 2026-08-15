import pygame
import sys
from core.game import SnakeGame, WIDTH, HEIGHT

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()
    game = SnakeGame(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.change_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    game.change_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    game.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    game.change_direction((1, 0))
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit(); sys.exit()

        game.update()
        game.draw()
        pygame.display.flip()
        clock.tick(game.speed)

        if game.game_over:
            print(f"Game Over! Final score: {game.score}")
            game.reset()

if __name__ == "__main__":
    main()