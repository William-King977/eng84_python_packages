from random import random # used to generate random numbers
import math

# print(random())

# Decimal rounding with math
num_float = 24.6
print("Actual float value " + str(num_float))
print(math.ceil(num_float)) # ceil() rounds up
print(math.floor(num_float)) # floor() rounds down


## Python Modules ##
import os
import platform
import datetime, sys

working_directory = os.getcwd() # gets the current directory
print(working_directory)

print(platform.uname())
print(os.cpu_count())
print(datetime.date.today())
print(sys.path)
print(math.pi) # pi







