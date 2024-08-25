from argparse import ArgumentParser
from memory_profiler import profile
from datetime import datetime

import sys
import os

DT = 1e5
NUM_STEPS = 10000000
NUM_PARTICLES = 2

DATA = (
    ((0.0, 0.0), (0.0, 0.0), 1.989e30),
    ((1.496e11, 0.0), (0.0, 29780.0), 5.972e24)
)

PROFILE_DIR = os.path.dirname(__file__)
CYTHON_PATH = "cython"


@profile
def run_pure():
    from pure_python.simulation import simulate, Particle, Vector

    particles = [Particle(Vector(_[0][0], _[0][1]), Vector(_[1][0], _[1][1]), _[2]) for _ in DATA]

    # TODO: please uncomment if you would like to profile python code with cProfile
    # from cProfile import Profile
    # from pstats import Stats, SortKey
    # profiler = Profile()
    # profiler.enable()

    ts = datetime.now()
    simulate(particles=particles, num_steps=NUM_STEPS, dt=DT)
    print(f"Total: {datetime.now() - ts}")

    # profiler.disable()
    # stats = Stats(profiler).sort_stats(SortKey.TIME)
    # stats.print_stats()


@profile
def run_cython():
    sys.path.append(os.path.abspath(os.path.join(PROFILE_DIR, CYTHON_PATH)))

    from cython.simulation import Vector, simulate_particles

    particles = [[Vector(_[0][0], _[0][1]), Vector(_[1][0], _[1][1]), _[2]] for _ in DATA]

    ts = datetime.now()
    simulate_particles(particles, NUM_STEPS, DT)
    print(f"Total: {datetime.now() - ts}")


@profile
def run_c_types():
    from c_types.simulation import lib, Particle, Vector

    particles = (Particle * NUM_PARTICLES)()

    for index, _ in enumerate(DATA):
        particles[index] = Particle(Vector(_[0][0], _[0][1]), Vector(_[1][0], _[1][1]), _[2])

    ts = datetime.now()
    lib.simulate(particles, NUM_PARTICLES, NUM_STEPS, DT)
    print(f"Total: {datetime.now() - ts}")


def main():
    parser = ArgumentParser(description="Profile different simulation modules.")
    parser.add_argument('--module', choices=['pure', 'cython', 'c_types'], required=True,
                        help="Specify the module to profile: 'pure', 'cython', or 'c_types'")
    args = parser.parse_args()

    if args.module == 'pure':
        run_pure()
    elif args.module == 'cython':
        run_cython()
    elif args.module == 'c_types':
        run_c_types()


if __name__ == '__main__':
    main()
