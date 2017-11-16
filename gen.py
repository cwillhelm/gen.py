#!/usr/bin/python

# This program generates a random password of length n
import string
import random
import sys

# dataset declaration
# some password forms don't take certain punctuation as input, change as necessary
chars = (string.ascii_letters + string.digits + '!@#$%^&*()_+=') 

# variable sys.argv length, no more than 3
length = len(sys.argv) 

# exit if user input was not input correctly
if length > 3:
    print ("Invalid argument. The syntax is gen.py <stringLength> <numberOfPasswords>")
    sys.exit(0)

# error handling, defaults to a string length of 14
try:
    n = int(sys.argv[1]) # string length
    x = int(sys.argv[2]) # number of passwords to generate
except IndexError:
    n = 14 # default to a string length of 14
    x = 1  # default to one password

print ('-' * n)

### TODO: Remove the blank line that appears after the - char

# generate a random string based on the length of the user input
for _ in range(x):
    print ('')
    for i in range(n):
        print ((random.SystemRandom().choice(chars)), end='') 