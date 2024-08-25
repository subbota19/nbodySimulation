import unittest

from python.src.pure_python.simulation import simulate, Vector, Particle


class TestPureSimulation(unittest.TestCase):

    def setUp(self):
        self.particles = [
            Particle(Vector(0.0, 0.0), Vector(0.0, 0.0), 1.989e30),  # Sun
            Particle(Vector(1.496e11, 0.0), Vector(0.0, 29780.0), 5.972e24)  # Earth
        ]

    def test_simulate_particles(self):
        simulate(self.particles)

        expected_positions = [
            Vector(241340.6, 8547825.5),  # Sun should remain at origin
            Vector(69220484399.0, 131110372783.9)  # Example final position for Earth
        ]

        # Compare the simulation results with the expected values

        self.assertAlmostEqual(self.particles[0].position.x, expected_positions[0].x, places=1)
        self.assertAlmostEqual(self.particles[0].position.y, expected_positions[0].y, places=1)

        self.assertAlmostEqual(self.particles[1].position.x, expected_positions[1].x, places=1)
        self.assertAlmostEqual(self.particles[1].position.y, expected_positions[1].y, places=1)


if __name__ == '__main__':
    unittest.main()
