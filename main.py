import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot


def main():
    print("Starting asteroids!")

    # Initiate pygame
    pygame.init()
    game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Create Player and Enemy Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    AsteroidField()

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, self.radius)

    def update(self, delta):
        self.position += self.velocity * delta

    updatable.add(player)
    drawable.add(player)

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        game_screen.fill("BLACK")
        dt = game_clock.tick(60) / 1000

        for thing in updatable:
            thing.update(dt)

        for thing in asteroids:
            if thing.collision_check(player):
                sys.exit("Game Over")

            for shot in shots:
                if thing.collision_check(shot):
                    shot.kill()
                    thing.split()

        for thing in drawable:
            thing.draw(game_screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
