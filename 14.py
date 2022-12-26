'''Write a Python program to find the second smallest number in a list.'''


n = int(input("Enter the number of elements you want:"))
l=[]

for i in range(n):
    ele = int(input("Enter the element : "))
    l.append(ele)
print ('My List: ',l)
sorted_list=l.sort()
print("Sorted List:",l)
#To convert given elements in ascending order
minimum_ele=l[0]
maximum_ele=l[-1]
second_smallest=l[1]
second_largest=l[-2]
#To print my list in sorting order
print("Minimum Element: ",minimum_ele)
print("Maximum Element: ",maximum_ele)
print("Second Smallest: ",second_smallest)
print("Second Largest: ",second_largest)
