from models.circleshape import CircleShape
from constants import SHOT_RADIUS
import pygame

class Shot(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", center=self.position, radius=SHOT_RADIUS, width=0)
    
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

