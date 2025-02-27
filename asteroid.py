import pygame
from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, kind):
        super().__init__(x, y, radius)
        self.kind = kind
        self.color = self.get_color()
        self.rotation_speed = random.uniform(-50, 50)
        self.angle = 0

    def get_color(self):
        # Different colors for different asteroid types
        colors = {
            1: "gray",
            2: "brown",
            3: "red",
            4: "black"
        }
        return colors.get(self.kind, "gray")

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt
        self.angle += self.rotation_speed * dt 

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius, self.kind)
        asteroid1.velocity = a * 1.2

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius, self.kind)
        asteroid2.velocity = b * 1.2
