"""
    NOTES: 
        cython is 

    We need also to setuptools and cythonize to compile the cython code. 

    Compile the cython code: 
        $python setup.py build_ext --inplace
"""

from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("sum_squares.py")
)

print('package initiated...')  
