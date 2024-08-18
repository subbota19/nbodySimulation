// simulation.c

#include <stdio.h>
#include <math.h>
#include "simulation.h"

// Function to subtract two vectors
Vector vector_sub(Vector a, Vector b) {
    Vector result;
    result.x = a.x - b.x;
    result.y = a.y - b.y;
    return result;
}

// Function to add two vectors
Vector vector_add(Vector a, Vector b) {
    Vector result;
    result.x = a.x + b.x;
    result.y = a.y + b.y;
    return result;
}

// Function to multiply a vector by a scalar
Vector vector_mul(Vector v, double scalar) {
    Vector result;
    result.x = v.x * scalar;
    result.y = v.y * scalar;
    return result;
}

// Function to divide a vector by a scalar
Vector vector_div(Vector v, double scalar) {
    Vector result;
    result.x = v.x / scalar;
    result.y = v.y / scalar;
    return result;
}

// Function to calculate the magnitude of a vector
double vector_magnitude(Vector v) {
    return sqrt(v.x * v.x + v.y * v.y);
}

// Function to compute forces on all particles
void compute_forces(Particle particles[], Vector forces[], int n) {
    for (int i = 0; i < n; i++) {
        forces[i] = (Vector){0.0, 0.0};  // Initialize force to zero
        for (int j = 0; j < n; j++) {
            if (i != j) {
                Vector displacement = vector_sub(particles[j].position, particles[i].position);
                double distance = vector_magnitude(displacement);
                if (distance != 0) {
                    double force_magnitude = G * particles[i].mass * particles[j].mass / (distance * distance);
                    Vector force_vector = vector_mul(vector_div(displacement, distance), force_magnitude);
                    forces[i] = vector_add(forces[i], force_vector);
                }
            }
        }
    }
}

// Function to update positions and velocities of particles
void update_positions_and_velocities(Particle particles[], Vector forces[], int n, double dt) {
    for (int i = 0; i < n; i++) {
        Vector acceleration = vector_div(forces[i], particles[i].mass);
        particles[i].velocity = vector_add(particles[i].velocity, vector_mul(acceleration, dt));
        particles[i].position = vector_add(particles[i].position, vector_mul(particles[i].velocity, dt));
    }
}

// Function to simulate the motion of particles
void simulate(Particle particles[], int num_particles, int num_steps, double dt) {
    Vector forces[num_particles];
    for (int step = 0; step < num_steps; step++) {
        compute_forces(particles, forces, num_particles);
        update_positions_and_velocities(particles, forces, num_particles, dt);
    }
}
