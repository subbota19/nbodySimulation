from _simulation import simulate_particles
from ctypes import Structure, c_double

NUM_STEPS = 1000
DT = 1e5


class Vector(Structure):
    _fields_ = [("x", c_double), ("y", c_double)]


# Initialize particles
particles = [
    [Vector(0.0, 0.0), Vector(0.0, 0.0), 1.989e30],  # Sun
    [Vector(1.496e11, 0.0), Vector(0.0, 29780.0), 5.972e24]  # Earth
]

# Call the Cython function
simulate_particles(particles, NUM_STEPS, DT)

# Output final positions of particles
for i, particle in enumerate(particles):
    pos = particle[0]
    print(f"Particle {i + 1} final position: x = {pos.x}, y = {pos.y}")
