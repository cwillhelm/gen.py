#!/usr/bin/python

# This program generates a random password of length n
import string
import secrets
import sys
import pyperclip as pc 

# dataset declaration
# some password forms don't take certain punctuation as input, change as necessary
chars = (string.ascii_letters + string.digits + '!@#$%^&*()_+=') 

# variable sys.argv length, no more than 3
length = len(sys.argv) 

#empty array to store passwords --- will be implemented later
l = 0
pw = [l]

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

### TODO: Remove the blank line that appears after the - char

# generate a random string based on the length of the user input
for _ in range(x):
    print ('')
    print ('-' * n)
    for i in range(n):
        print ((secrets.SystemRandom().choice(chars)), end='') 

print ('')
print ('-' * n)