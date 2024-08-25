from typing import List

# Constants
G: float = 6.67430e-11  # Gravitational constant
DT: float = 1e5  # Time step (seconds)
NUM_STEPS: int = 1000  # Run simulation


class Vector:
    def __init__(self, x: float = 0, y: float = 0):
        self.x: float = x
        self.y: float = y

    def __sub__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x - other.x, self.y - other.y)

    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar: float) -> 'Vector':
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar: float) -> 'Vector':
        return Vector(self.x / scalar, self.y / scalar)

    def magnitude(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __repr__(self) -> str:
        return f"Vector(x={self.x}, y={self.y})"


class Particle:
    def __init__(self, position: Vector, velocity: Vector, mass: float):
        self.position: Vector = position
        self.velocity: Vector = velocity
        self.mass: float = mass


def compute_forces(particles):
    forces = [Vector() for _ in particles]
    for _i, particle_i in enumerate(particles):
        for _j, particle_j in enumerate(particles):
            if _i != _j:
                displacement = particle_j.position - particle_i.position
                distance = displacement.magnitude()
                if distance != 0:
                    force_magnitude = G * particle_i.mass * particle_j.mass / distance ** 2
                    force_vector = displacement / distance * force_magnitude
                    forces[_i] += force_vector

    return forces


def update_positions_and_velocities(particles: List[Particle], forces: List[Vector], dt: float):
    for _, _particle in enumerate(particles):
        acceleration = forces[_] / _particle.mass
        _particle.velocity += acceleration * dt
        _particle.position += _particle.velocity * dt


def simulate(particles: List[Particle], num_steps: int = NUM_STEPS, dt: float = DT):
    for _ in range(num_steps):
        forces: List[Vector] = compute_forces(particles)
        update_positions_and_velocities(particles, forces, dt)
