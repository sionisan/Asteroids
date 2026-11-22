import pygame
import random
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen:pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position = self.position + (self.velocity * dt)

    def split(self, ):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            r = random.uniform(20, 50)
            a1 = self.velocity.rotate(r)
            a2 = self.velocity.rotate(-r)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            Ast1 = Asteroid(self.position.x, self.position.y, new_radius)
            Ast1.velocity = a1
            Ast2 = Asteroid(self.position.x, self.position.y, new_radius)
            Ast2. velocity = a2
