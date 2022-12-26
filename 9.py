'''Write a Python function that takes two lists and returns true if they have 
   at least one common member.'''

list1=[1,3,5,7]
list2=[2,8,4,7]
result = 0
def find_common(list1, list2):
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result
     else:
        result = False
        return result
print(find_common(list1, list2))
