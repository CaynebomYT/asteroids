import pygame
from constants import *
from player import *
from circleshape import *

def main():
    pygame.init()
    fpsClock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player_x_start = (SCREEN_WIDTH / 2)
    player_y_start = (SCREEN_HEIGHT / 2)
    player = Player(player_x_start, player_y_start)
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        dt = ((fpsClock.tick(60))/1000)




if __name__ == "__main__":
    main()
 