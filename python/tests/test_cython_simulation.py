import unittest
import sys
import os

TEST_DIR = os.path.dirname(__file__)
CYTHON_PATH = "src/cython"

sys.path.append(os.path.abspath(os.path.join(TEST_DIR, '..', CYTHON_PATH)))

from python.src.cython.simulation import simulate_particles, Vector


class TestCythonSimulation(unittest.TestCase):

    def setUp(self):
        self.num_steps = 1000
        self.dt = 1e5
        self.particles = [
            [Vector(0.0, 0.0), Vector(0.0, 0.0), 1.989e30],  # Sun
            [Vector(1.496e11, 0.0), Vector(0.0, 29780.0), 5.972e24]  # Earth
        ]

    def test_simulate_particles(self):
        # Call the Cython function
        simulate_particles(self.particles, self.num_steps, self.dt)

        expected_positions = [
            Vector(241340.6, 8547825.5),  # Example final position for Sun
            Vector(69220484399.0, 131110372783.9)  # Example final position for Earth
        ]

        # Compare the simulation results with the expected values
        self.assertAlmostEqual(self.particles[0][0].x, expected_positions[0].x, places=1)
        self.assertAlmostEqual(self.particles[0][0].y, expected_positions[0].y, places=1)

        self.assertAlmostEqual(self.particles[1][0].x, expected_positions[1].x, places=1)
        self.assertAlmostEqual(self.particles[1][0].y, expected_positions[1].y, places=1)


if __name__ == '__main__':
    unittest.main()
