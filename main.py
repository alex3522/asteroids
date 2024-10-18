import pygame
from constants import *
from player import *
def main():
    pygame.init()
    Clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)
        screen.fill("#000000")
        player.draw(screen)
        pygame.display.flip()

        dt = Clock.tick(60) /1000

if __name__ == "__main__":
    main()