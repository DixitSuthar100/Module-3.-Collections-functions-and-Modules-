'''Write a Python program to create a dictionary from a string. 
   Note: Track the count of the letters from the string. 
   Sample string: 'w3resource' 
   Expected output: 
        {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1} '''


str = input("Enter a string: ")
dic = {} #creates an empty dictionary
for chr in str:
    if chr in dic: #if next character is already in the dictionary
        dic[chr] += 1
    else:
        dic[chr] = 1 #if ch appears for the first time
for key in dic:
    print(key,':',dic[key])
