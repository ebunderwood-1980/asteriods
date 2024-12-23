from circleshape import CircleShape
from constants import RED, SHOT_RADIUS
import pygame


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, RED, self.position, self.radius)

    def update(self, delta):
        self.position += self.velocity * delta
