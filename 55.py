'''Write a Python program to read a random line from a file.'''

import random

file=open("tops.text","r")
print(file.read())
file.close()
