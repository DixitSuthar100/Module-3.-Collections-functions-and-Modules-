'''Write a Python program to check whether an element exists within a 
   tuple'''

tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
print("r" in tuplex)
print(2 in tuplex)

print("*"*40)

'''using for loop'''

my_tuple_1 = (23, 45, 12, 56, 78, 0)

print("The first tuple is : ")
print(my_tuple_1)
N = 12
print("The value of 'N' has been initialized")

my_result = False
for elem in my_tuple_1 :
   if N == elem :
      my_result = True
      break
print("tuple contain the value mentioned is :",my_result)
