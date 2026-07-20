import random

from logger import log_event
from models.circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
import pygame

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", center=self.position, radius=self.radius, width=LINE_WIDTH)
    
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
    
    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        rand = random.uniform(20, 50)
        vec1 = self.velocity.rotate(rand)
        vec2 = self.velocity.rotate(-rand)
        
        newRadius = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid1 = Asteroid(self.position.x, self.position.y, newRadius)
        asteroid2 = Asteroid(self.position.x, self.position.y, newRadius)
        asteroid1.velocity = vec1 * 1.2
        asteroid2.velocity = vec2 * 1.2
        
