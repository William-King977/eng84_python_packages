# Python Packages
## What is a package?
A package is a collection of Python modules, so it is 
basically a hierarchical file directory structure of 
Python modules and subpackages that has an 
`__init__.py` file to distinguish it from a "normal" 
file directory.

They can be used with the following command:
```python
# importing datetime package
import datetime
```

### Why should we use them?
Python packages allow you to break down large programs 
and organise their modules in a consistent way, so that 
they can be used and reused efficiently. 

### What is pip?
`pip` is a package manager in Python that allows you to 
install and manage additional packages that are not part 
of the Python standard library.
 * To use pip `pip install package_name`
 * E.g. `pip3 install requests`

### Python Modules
A Python module is a file containing Python definitions, 
statements and functions. Any Python file is a module. 
These can be imported into a Python file for added 
functionality without the need of repeating code.

```python
# importing date module from datetime package
from datetime import date

# you can import your own python files in the same directory
import my_file
```