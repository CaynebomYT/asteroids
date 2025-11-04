import pygame
import sys
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    fpsClock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    dt = 0
    
    player_x_start = (SCREEN_WIDTH / 2)
    player_y_start = (SCREEN_HEIGHT / 2)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    belt = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (belt, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (bullets, updatable, drawable)

    field = AsteroidField()
    player = Player(player_x_start, player_y_start)
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for item in drawable:
            item.draw(screen)
        updatable.update(dt)
        for rock in belt:
            if rock.collide(player):
                print("Game Over!")
                sys.exit()
        for rock in belt:
            for shot in bullets:
                if rock.collide(shot):
                    rock.split()
        pygame.display.flip()
        dt = ((fpsClock.tick(60))/1000)




if __name__ == "__main__":
    main()
 