# Setup tools package :) 
We can use this library to build  C Python extension module using cython too  
setuptools used to build, package, install and distribute python packages

what we can do with setup : 

- Install the project (pip install .)
- Build Cython extensions (build_ext) means compiling them
- Package the project (`sdist`, `bdist_wheel`)
- Distribute it on PyPI (using `twine`)
- Define dependencies (install_requires=["numpy"])
- Specify metadata (name, version, author, etc.)  
<br> 


> :warning: setup and requirement.txt don't serve same thing  
> - requirements.txt is better for deployemenet and stuff like that, as we can use `$pip freeze > requirements.txt`   
> - setuptools is for packaging and distribution 


This is like a very long description to be used 

## Extra Informations
Chat gpt saying folder structure shoud be like this :  

    my_project/
    │── src/                      # Source code (optional, but recommended)
    │   ├── my_package/           # Your actual Python package
    │   │   ├── __init__.py       # Marks this as a package
    │   │   ├── module1.py        # Example module
    │   │   ├── module2.py        # Another module
    │── tests/                    # Unit tests
    │   ├── test_module1.py       # Tests for module1
    │   ├── test_module2.py       # Tests for module2
    │── pyproject.toml            # Modern build system config (recommended)
    │── setup.py                  # (Legacy) Setup script for setuptools
    │── setup.cfg                 # Configuration for setuptools
    │── MANIFEST.in               # Extra files to include in the package
    │── README.md                 # Project description
    │── LICENSE                   # License file
    │── requirements.txt           # Dependencies (if applicable)

Using a src/ directory for your source code helps prevent accidental imports of the local package when running tests or scripts outside a virtual environment. Because By default, when you run Python scripts, Python looks for modules in:
- The current directory (where the script is run).
- The Python environment's site-packages.

# How to package and publish your code
tutorial from : https://www.youtube.com/watch?v=5KEObONUkik&ab_channel=ArjanCodes

> **:memo: NOTE** this is not 100% following the tutorial, as I change lot of stuff to adapt it for a better documentation 



wheel : binary distribution 


### Source distribution `$python setup.py sdist`
it creates a source distrubition file `.tar.gz` file udner the `dist` folder

### Binary distribution `$python setup.py bdist_wheel`  
binary distribution 
- it creates the `build` and `dist` folders   
- `dist` folder we will get the `.whl `that is the binary file that contains everything
- Generates a .whl (wheel file), which is a pre-built package.
- Faster installation because it skips compilation.

### `$pip install .` 
 to install the package locally and adding it to site-packages for testing purposes, before throwing it in pip


### $pip install mypackage.whl
Installs the wheel without needing to compile anything.
This is why many PyPI packages provide wheels for different OSs.


<br>  

## To build a Cython file : 
`$ python setup.py build_ext --inplace `    
Compiles Cython (.pyx) files into `shared libraries` (`.so` or `.pyd`).  
`--inplace` means the compiled files stay in the source directory instead of a build folder.


- it creates a .c and .pyd files  
- use Extension class as shown in the example, to not fall in the error, of nested paths, since cythonize will try to put that whole path in the specified directory. But there is a conflict that will arise as we specify the package:'src' in setup() so it will try to put src/name.pyd inside src resulting in src/src/...
solution is to explicitly use extension as we set the name apart and the sources apart. 


    

<br>
## PyPI
I leave this section for later usage as I don't really want it to be used now ! 

<br>

### pyproject.toml 
this will let us not use setuptools at all, 
here an example pyproject.tom file 

```py 
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "my_project"
version = "0.1.0"
description = "A sample project"
dependencies = [
    "numpy>=1.21",
    "pandas>=1.3,<2.0",
    "scipy>=1.5,<1.10"
]

[tool.setuptools]
packages = ["my_package"]  # Define the package location
```
and this typically runs with 
- $pip install .





## some other informations about compiled python compiled cython ...

- python `bytecode compilation` .py -> .pyc (the bytecote runs on python virtual machine)
- `cython` compilation .py -> .c -> .so/.pyd can be imported directly to python like a module
    - the compiled code runs directly in the cpu bpassing python interpreter
    - we use setuptools library and cython to compile it 

