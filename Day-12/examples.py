# DAY 12 : MODULES

# WHAT IS A MODULE?
# A module is a file containing a set of codes or a set of functions which can be
# included to an application. A module could be a file containing a single variable,
# a function or a big code base

# CREATING A MODULE
# To create a module we write our codes in a python script and we save it as a .py file.
# Create a file named mymodule.py inside your project folder. Let's write some code in
# this file. Create also another file: main.py in your folder and import the mymodule.py
# file

# IMPORTING A MODULE
# To import the file we use the import keyword and the name of the file only
# example: import mymodule

# IMPORT FUNCTIONS FROM A MODULE
# We can have many functions in a file and we can import all the functions differently
# example: from mymodule import generate_full_name, sum_two_nums, person, gravity

# IMPORT FUNCTIONS FROM A MODULE AND RENAMING
# During importing we can rename the functions and variables
# example: from mymodule import generate_full_name as fullname

# IMPORT BUILT-IN MODULES
# Like other programming languages, we can also import modules by importing the 
# file/function using the keyword IMPORT. Let's import the common module we will use
# most of the time. 
# Some of the common built-in modules: math, datetime, os, sys, random, statistics,
#                                      collections, json, re

# OS MODULE
# Using python os module it is possible to automatically perform many operating system
# tasks. The OS module in python provides functions for creating, changing current working
# directory, removing a directory (folder), fetching its contents, amd changing and identifying
# the current directory

# import the module
import os
# Changing the current directory
os.chdir('Day-12')
# Creating a dictionary
print('creating the directory')
os.mkdir('directory_name')
# Getting current working directory
os.getcwd()
# Removing directory
print('removing the directory')
os.rmdir('directory_name')

# SYS MODULE
# The sys module provides functions and variables used to manipulate different parts of
# the Python runtime environment. Function sys.argv returns a list of command line
# arguments passed to a Python script. The item at index 0 in this list is always the
# name of the script, at index 1 is the argument passed from the command line

print('-----------------------------')

# Example of a examples.py file:
import sys
# print(sys.argv[0], sys.argv[1], sys.argv[2]) # this line would print> filename arg1 arg2
# print('Welcome {}. Enjoy {} challenge!'.format(sys.argv[1], sys.argv[2]))

# Some useful sys commands: (work only on command line?)
# To exit sys
# sys.exit()
# To know the largest integer variable it takes
sys.maxsize
# To know environment path
sys.path
# To know the version of python you are using
sys.version

print('-----------------------------')

# STATISTICS MODULE
# The statistics module provides functions for mathematical statistics of numeric data.
# The popular statistical functions which are defined in this module: mean, median, mode,
# stdev etc.
from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages))

print('-----------------------------')

# MATH MODULE
# Module containing many mathematical operations and constants
import math
print(math.pi)          # 3.14..., pi constant
print(math.sqrt(2))     # 1.41421..., square root
print(math.pow(2, 3))   # 8.0, exponential function
print(math.floor(9.81)) # 9, rounding to the lowest
print(math.ceil(9.81))  # 10, rounding to the highest
print(math.log10(100))  # 2, logarithm with 10 as a base

print('-----------------------------')

# Now we have imported the math module which contains lots of functions which can help
# us to perform mathematical calculations. To check what functions the module has got,
# we can use help(math) or dir(math). This will display the available functions in the
# module. If we want to import only a specific function from the module we import it
# as follows:
from math import pi
print(pi)

print('-----------------------------')

# It is also possible to import multiple functions at once
from math import pi, sqrt, pow, floor, ceil, log10
print(pi)
print(sqrt(2))
print(pow(2, 3))
print(floor(9.81))
print(ceil(9.81))
print(log10(100))

print('-----------------------------')

# But if we want to import all the function in math module, we can use *
from math import *
print(pi)

print('-----------------------------')

# When we import we can also rename the name of the function
from math import sqrt as juuri
print(juuri(4))

print('-----------------------------')

# STRING MODULE
# A string module is a useful module for many purposes. The example below shows some
# uses of the string module
import string
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

print('-----------------------------')

# RANDOM MODULE
# By now you are familiar with importing modules. Let us do one more import to get very
# familiar with it. Let us import random module which gives us a random number between
# 0 and 0.99999... The random module has lots of functions but in this section we will
# only use random and randint
from random import random, randint
print(random())         # doesn't take any arguments, returns a value between 0 and 0.999..
print(randint(5, 20))   # returns random integer number between [5, 20] inclusive

print('-----------------------------')
