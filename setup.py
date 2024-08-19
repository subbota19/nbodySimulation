from setuptools import setup
from Cython.Build import cythonize
from setuptools.extension import Extension
from os.path import relpath, dirname, join as path_join
from typing import List

PACKAGE_DIR = relpath(dirname(__file__))

print(PACKAGE_DIR)


# Define the extension module

def get_extension() -> List[Extension]:
    sources = [
        path_join(PACKAGE_DIR, "python", "src", "cython", "_simulation.pyx"),
        path_join(PACKAGE_DIR, "c", "src", "simulation.c"),
    ]
    return [
        Extension(
            name="python.src.cython._simulation",
            # sources=["python/src/cython/_simulation.pyx"],
            sources=sources,
            include_dirs=["c/include"],
            extra_compile_args=["-fPIC"],
            extra_link_args=["-lm"],
        )
    ]


# Setup script
setup(
    ext_modules=cythonize(get_extension())
)
