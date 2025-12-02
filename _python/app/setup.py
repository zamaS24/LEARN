from setuptools import find_packages, setup, Extension
from Cython.Build import cythonize



with open("README.md", "r") as f: 
    long_description = f.read() 

# because cythonize() by default creates the compiled .pyd file in the same directory where the .pyx file is located unless a custom build_ext path is specified.

ext_modules = [
    Extension(
        name="hellocython",  # Name of the compiled extension module
        sources=["src/hellocython.py"],  # The source .pyx file
    )
]

setup(
    name="fibonnaci",
    version="0.1.0",
    # description='A package for doing ... A and B and C ... for Z and all.. just for testing purposes',
    
    # packages=find_packages(where="src"),
    package_dir={"": "src"},
    
    # long_description=long_description,
    # long_description_content_type='text/markdown',
    # author='Hamza OMARI',
    # author_email='omarihamza2000@gmail.com',
    license='MIT',

    ext_modules=cythonize(ext_modules),
    # ext_modules=cythonize('src/hellocython.py'), 

    install_requires=[
        "numpy",
        "pandas",
    ],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"]
    },
    python_requires=">=3.10",
)


if __name__ == '__main__': 
    pass

    










