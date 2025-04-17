import sys
import pygame
from constants import * 
from player import *
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    pygame.init()
    clock = pygame.time.Clock()
    
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroids, updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group)
    Shot.containers = (updatable_group, drawable_group, shots)
    

    asteroid_field = AsteroidField()
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    
    dt = 0
    FPS = 180

    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))
        for drawable in drawable_group:
            drawable.draw(screen)
        pygame.display.flip()
        updatable_group.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()

                
    
        dt = clock.tick(FPS) / 1000

if __name__ == "__main__":
    main() 
