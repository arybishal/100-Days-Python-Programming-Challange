# 1. build in modules (The built-in Python functions are pre-defined by the python interpreter. There are 68 built-in python functions. These functions perform a specific task and can be used in any program, depending on the requirement of the user.)
# 2. External modules ( External modules have to be downloaded externally; they are not already present like the built-in ones. Installing them is a rather easy task and can be done by using the command “pip install module_name” in the compiler terminal.)



import pandas  # This is an example of external module
import hashlib  # This is an example of built in module

print("Hi")

# Dont worry about how to use these modules just yet!
pandas.read_csv("example.csv")
m = hashlib.sha256()
