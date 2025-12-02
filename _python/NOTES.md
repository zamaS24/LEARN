# Sommaire
-
-
-
<br>

# 1. Récupérer les argumets passer par la console
```py
import sys
for argv in sys.argv: 
    print(f"{argv}")
```


example:  
```py
if len(sys.argv) < 2:
    print("Please provide the video name as an argument.")
    sys.exit()
```
__*NB*__  ``sys.argv`` contient notamment comme premier argument le nom du scipt executé.
 

<br>  

# 2. Shebang Line & character encoding comment
 
- `#!/usr/bin/env python`  
Shebang Line (#!/usr/bin/env python): Even though #!/usr/bin/env python appears as a comment within the Python code, the operating system recognizes it as a special directive. When you execute a script file from the command line, the operating system examines the first line of the file. If it begins with #! (shebang), the OS interprets the rest of the line as the path to the interpreter that should be used to run the script. In this case, /usr/bin/env python is used to locate the Python interpreter, and the script is executed using that interpreter.

- `# -*- coding: utf-8 -*-`  
Character Encoding Comment  This comment specifies the character encoding of the source code in the file. While it is a comment within the Python code, it's used by some tools (including Python itself) to correctly interpret the characters in the file. 

<br>

# 3. Abstract Classes in python
### Abstract Classes in OOP   
An abstract class is a class that cannot be instantiated directly and is meant to serve as a blueprint or template for other classes. It often contains abstract methods, which are methods that are declared but do not contain any implementation in the abstract class itself. Instead, concrete (sub)classes that inherit from the abstract class must provide implementations for these abstract methods.

__*keypoints*__
- __Cannot be Instantiated__
    you cannot create an instance of an abstract class directly. It's meant to be subclassed. 
- __May Contain Concrete Methods__
    An abstract class can have both abstract methods (without implementation) and concrete methods (with implementation).
- __Forcing Subclasses to Implement Methods__ Abstract classes often contain abstract methods that subclasses must implement. This enforces a contract that ensures specific methods are present and functional in all subclasses.

### Implementation
```py 
from abc import ABC, abstractmethod
```
__then__
```py 
class MyAbstractClass(ABC):
    @abstractmethod
    def my_abstract_method(self):
        pass

    def my_concrete_method(self):
        return "This is a concrete method."
```
__Subclass the abstract class and provide implementations for abstract methods:__
```py 
class MySubclass(MyAbstractClass):
    def my_abstract_method(self):
        return "Implementation of the abstract method."

# This will work
subclass_instance = MySubclass()
print(subclass_instance.my_abstract_method())  # Output: "Implementation of the abstract method."
print(subclass_instance.my_concrete_method())  # Output: "This is a concrete method."

# This will raise a TypeError since the abstract method is not implemented
another_instance = MyAbstractClass()  # Raises TypeError
```
<br>

# 4. Convention underscore _
By convention, when a method is prefixed with an underscore _, it is a signal that the method is intended for internal use within the class and is not part of the public API. This is a way to indicate that the method is meant to be called only within the class and should not be relied upon or called from outside the class.

```py
class MyClass:
    def __init__(self):
        self._variable = 10

    def _internal_method(self):
        return self._variable + 5

    def public_method(self):
        result = self._internal_method()
        return result * 2
```
Remember that these conventions are not enforced by the language itself, and Python doesn't prevent you from accessing methods or attributes with leading underscores. However, following these conventions makes your code more readable and helps communicate your intentions to other developers who might be using or maintaining your code.

<br>

# 5. Dunder (magic) methods


<br>


# 6. Virtal environement and requirements.txt

### Create a virtual environement

```bash
python -m venv venv
```

### Activate the Virtual Environment (Optional but Recommended)

```bash
venv\Scripts\activate
```

### Install project dependencies
```bash
pip install -r requirements.txt
```

### Deactivate the Virtual Environment (Optional but Recommended)

> :warning: **Warning**<br>
> Yo must use `cmd` so this can work. 

```cmd
cd venv\Scripts
deactivate
```

# Make a python poject folder executable
instead of having the entroypoint script named a certain name and to execute it it will require to execute python name_script.py.

we would just name it ``__main__.py`` and then in the command line just do `python project.py` 

this will be an elegant way to execute python projects

