// simulation.h

#ifndef SIMULATION_H
#define SIMULATION_H

// Constants
#define G 6.67430e-11  // Gravitational constant
#define DT 1e5  // Time step (seconds)
#define NUM_STEPS 1000  // Number of steps in the simulation

// Vector structure definition
typedef struct {
    double x;
    double y;
} Vector;

// Particle structure definition
typedef struct {
    Vector position;
    Vector velocity;
    double mass;
} Particle;

// Function prototypes
Vector vector_sub(Vector a, Vector b);
Vector vector_add(Vector a, Vector b);
Vector vector_mul(Vector v, double scalar);
Vector vector_div(Vector v, double scalar);
double vector_magnitude(Vector v);
void compute_forces(Particle particles[], Vector forces[], int n);
void update_positions_and_velocities(Particle particles[], Vector forces[], int n, double dt);
void simulate(Particle particles[], int num_particles, int num_steps, double dt);

#endif
