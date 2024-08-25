# N-Body Simulation Project

## Overview

This project implements an N-Body simulation to model and analyze the movement of celestial bodies under the influence of gravitational forces. The simulation can be executed using three different computational approaches to estimate performance and accuracy:

**Pure Python**: A straightforward implementation using Python classes and functions.
**Cython**: A hybrid approach that compiles Python code to C for improved performance.
**C with ctypes**: Utilizes a shared C library to perform the computation, invoked from Python using the `ctypes` library.

Each implementation is designed to be interchangeable, allowing for easy comparison and profiling of different methods.

## Features

- **N-Body Simulation**: Models the gravitational interaction between bodies.
- **Computational Approaches**:
  - **Pure Python**: Easy to understand but may be slower.
  - **Cython**: Provides performance improvements by compiling Python code.
  - **C with ctypes**: Uses a C library for computation, called from Python.
- **Testing**: Ensures that all implementations produce consistent results.
- **Profiling**: A core profiling script to analyze performance and memory usage, including `cProfile`, `memory_profiler` and `Manual Timing`.

## Testing

Each implementation is thoroughly tested to ensure that the logic is consistent across all approaches. Tests are located in the tests directory and validate that the behavior and results of the simulation are correct and consistent.

`python -m unittest discover python/tests/`

## Profiling Script

The profiler.py script is used to profile various modules. You can specify which module to profile using the --module argument:

`python profiler.py --module pure`

`python profiler.py --module cython`

`python profiler.py --module ctypes`


