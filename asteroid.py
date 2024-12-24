from circleshape import CircleShape
import pygame
from constants import GREEN, ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, GREEN, self.position, self.radius)

    def update(self, delta):
        self.position += self.velocity * delta

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_one.velocity = self.velocity.rotate(-1 * random_angle) * 1.2
            asteroid_two.velocity = self.velocity.rotate(random_angle)
