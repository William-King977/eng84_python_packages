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

### Python Modules
A Python module is a file containing Python definitions, 
statements and functions. Any Python file (.py) is a Python
module. These can be imported into a Python file for added 
functionality without the need of repeating code.

```python
# importing date module from datetime package
from datetime import date

# you can import your own python files in the same directory
import my_file
```

### What is pip?
`pip` is a package manager in Python that allows you to 
install and manage additional packages that are not part 
of the Python standard library.
 * To update pip: `python -m pip install --upgrade pip`
 * To use pip: `pip install package_name`
   * E.g. `pip3 install requests`
    
## Application Programming Interface (API)
### What is an API?
An API is a set of definitions and protocols that allow 
software products and services to communicate with each other 
via the internet. Essentially, it is the messenger that runs 
and delivers your request to the provider you're requesting 
it from, and then delivers the response back to you. 

An example with the Python `requests` module is shown below:
```python
  import requests # allows you to send HTTP requests
    
  response = requests.get("http://www.bbc.co.uk/")
    
  # Status (code) 200 means the website is live and running
  # Status (code) 400 or 404 means not working
  if response:
      print(f"Success {response.status_code}.")
  else:
      print(f"Oops, something went wrong {response}.")
  ```

### Why should we use them?
* Using APIs makes it possible to integrate different 
  systems together. For example, an API can be used to 
  enable a Customer Relationship Management (CRM) system and 
  a Marketing Automation system to communicate with each other, 
  so that you can send a marketing email when a sales 
  representative adds a new customer on a CRM.
* APIs can be used to add functionalities for improving 
  customer experience and interaction with the organisation. 
  For example, using an API to automatically notify the 
  customer when their delivery has been dispatched.
* APIs can help reduce software development costs by allowing 
  developers to build reusable components. For example, a 
  backend developer can create a system that holds 
  information about customers. Then other developers across 
  the organisation can use APIs to grab that information 
  and track payments for finance and accounts payable, help 
  customer service resolve problems faster, or even create 
  recommendations for marketing campaigns.