// main.c

#include <stdio.h>
#include "simulation.h"

int main() {
    // Initialize particles
    Particle particles[] = {
        {{0.0, 0.0}, {0.0, 0.0}, 1.989e30},         // Sun
        {{1.496e11, 0.0}, {0.0, 29780.0}, 5.972e24}  // Earth
    };
    int num_particles = sizeof(particles) / sizeof(Particle);

    // Run simulation
    simulate(particles, num_particles, NUM_STEPS, DT);

    // Output final positions of particles
    for (int i = 0; i < num_particles; i++) {
        printf("Particle %d final position: x = %e, y = %e\n", i + 1, particles[i].position.x, particles[i].position.y);
    }

    return 0;
}
