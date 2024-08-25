from ctypes import c_double, c_int, POINTER, CDLL, Structure

CDLL_PATH = "./simulation-shared.so"

NUM_PARTICLES = 2
NUM_STEPS = 1000
DT = 1e5

# Load the shared library
lib = CDLL(CDLL_PATH)


class Vector(Structure):
    # attribute that specifies the fields of the C-style structure.
    _fields_ = [("x", c_double), ("y", c_double)]


class Particle(Structure):
    # attribute that specifies the fields of the C-style structure.
    _fields_ = [("position", Vector), ("velocity", Vector), ("mass", c_double)]


# Define argument and return types for the functions
lib.compute_forces.argtypes = [POINTER(Particle), POINTER(Vector), c_int]
lib.update_positions_and_velocities.argtypes = [POINTER(Particle), POINTER(Vector), c_int, c_double]
lib.simulate.argtypes = [POINTER(Particle), c_int, c_int, c_double]

# Initialize particles
particles = (Particle * NUM_PARTICLES)()
particles[0] = Particle(Vector(0, 0), Vector(0, 0), 1.989e30)  # Sun
particles[1] = Particle(Vector(1.496e11, 0), Vector(0, 29780), 5.972e24)  # Earth

# Run the simulation
lib.simulate(particles, NUM_PARTICLES, NUM_STEPS, DT)
