from libc.stdlib cimport malloc, free
from libc.string cimport memset

cdef struct Vector:
    double x
    double y

cdef struct Particle:
    Vector position
    Vector velocity
    double mass

# Import C functions and C data types:
# block use definitions from an external C header file.
# This allows declare C functions, structs, constants.
cdef extern from "simulation.h":
    void simulate(Particle particles[], int num_particles, int num_steps, double dt)

# Wrapper function for Python
def simulate_particles(list particles, int num_steps, double dt):
    cdef int num_particles = len(particles)
    cdef Particle *c_particles = <Particle *> malloc(num_particles * sizeof(Particle))
    cdef Vector *forces = <Vector *> malloc(num_particles * sizeof(Vector))

    if c_particles == NULL or forces == NULL:
        raise MemoryError("Failed to allocate memory for particles or forces.")

    # Initialize memory for forces
    memset(forces, 0, num_particles * sizeof(Vector))
    memset(c_particles, 0, num_particles * sizeof(Particle))

    # Convert Python list to C array
    for i in range(num_particles):
        c_particles[i].position.x = particles[i][0].x
        c_particles[i].position.y = particles[i][0].y
        c_particles[i].velocity.x = particles[i][1].x
        c_particles[i].velocity.y = particles[i][1].y
        c_particles[i].mass = particles[i][2]

    # Call the C function
    simulate(c_particles, num_particles, num_steps, dt)

    # Convert C array back to Python list
    for i in range(num_particles):
        particles[i][0].x = c_particles[i].position.x
        particles[i][0].y = c_particles[i].position.y
        particles[i][1].x = c_particles[i].velocity.x
        particles[i][1].y = c_particles[i].velocity.y
        particles[i][2] = c_particles[i].mass

    # Free allocated memory
    free(c_particles)
    free(forces)