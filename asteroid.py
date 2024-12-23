from circleshape import CircleShape
import pygame
from constants import WHITE


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, self.radius)

    def update(self, delta):
        self.position += self.velocity * delta
