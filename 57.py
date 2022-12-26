
'''Write a Python program to calculate the area of a trapezoid '''


# Python Program to find Area of a Trapezoid

base1 = float(input('Please Enter the First Base of a Trapezoid: '))
base2 = float(input('Please Enter the Second Base of a Trapezoid: '))
height = float(input('Please Enter the Height of a Trapezoid: '))

# calculate the area
area = ((base1 + base2)/2) * height
print("Area is:", area)
