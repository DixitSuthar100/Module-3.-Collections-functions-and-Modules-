'''Write a Python program to convert a tuple to a string.'''

tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
str =  ''.join(tup)
print(str)


'''Convert a tuple to a string using for loop method'''


# Defining a Python tuple
tup = ('Linux', 'for', 'Devices')
 
# Creating an empty Python string
str = ''
 
# Using the Python for loop to convert the tuple to a string
for i in tup:
    str = str + i
 
# Printing the results
print("Given Python tuple: ", tup)
print("Generated Python string: ", str)
 
# Validating the type of 'st'
print(type(str))
