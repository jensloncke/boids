import random
from typing import List
from pygame.math import Vector2

class Boid:
    def __init__(self):
        self.position = Vector2(random.random(), random.random())
        self.velocity = Vector2(random.random(), random.random()) * 0.1

    def update_velocity(self, neighbours: List["Boid"]):
        dv_seperation = self.dv_seperation(neighbours)
        dv_alignment = self.dv_alignment(neighbours)
        dv_cohesion = self.dv_cohesion(neighbours)
        self.velocity += dv_seperation + dv_alignment + dv_cohesion

    def dv_seperation(self, neighbours: List["Boid"]):
        pass

    def dv_alignment(self, neighbours: List["Boid"]):
        pass

    def dv_cohesion(self, neighbours: List["Boid"]) -> Vector2:
        com = Vector2(0, 0)
        for boid in neighbours:
            com += boid.position
        com /= len(neighbours)

        return (com - self.position) * 0.1


