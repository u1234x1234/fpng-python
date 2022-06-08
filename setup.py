from setuptools import setup, Extension

# Compile *mysum.cpp* into a shared library 
setup(
    name='pyfpng',
    version='0.1',
    description='Python bindings for fpng',
    author='Oskar Vuola',
    packages=['pyfpng'],
    ext_modules=[Extension('pyfpng.libpyfpng', ['src/fpng_py.cpp', 'fpng/src/fpng.cpp'], include_dirs=['fpng/src/'], extra_compile_args=['-msse4.1', '-mpclmul', '-fno-strict-aliasing'])]
)
