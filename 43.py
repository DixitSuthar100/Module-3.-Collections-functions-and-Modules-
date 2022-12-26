'''Write a Python program to find the highest 3 values in a dictionary''' 



dic = {"A":12,"B":13,"C":9,"D":89,"E":34,"F":17,"G":65,"H":36,"I":25,"J":11,"K":100}

#Creating an empty list to store all the values of the dictionary
lst = list()

#Looping through each values and storing it in list
for a in dic.values():
    
    lst.append(a)

#Sorting the list in ascending order, it will store the highest value at the last index
    lst.sort()

print("Highest value:",lst[-1])
print("Second highest value:",lst[-2])
print("Third highest value:",lst[-3])
