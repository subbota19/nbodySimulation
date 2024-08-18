from setuptools import setup
from Cython.Build import cythonize
from setuptools.extension import Extension

# Define the extension module
ext_modules = [
    Extension(
        name="simulation",
        sources=["python/src/cython/simulation.pyx"],
        include_dirs=["c/include"],
        libraries=["simulation"],
        library_dirs=["."],
        extra_compile_args=["-fPIC"],
        extra_link_args=["-lm"]
    )
]

# Setup script
setup(
    ext_modules=cythonize(ext_modules)
)
