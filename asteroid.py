from circleshape import CircleShape
import pygame
from constants import GREEN


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, GREEN, self.position, self.radius)

    def update(self, delta):
        self.position += self.velocity * delta

    def split(self):
        self.kill()
