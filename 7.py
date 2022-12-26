'''Write a Python program to remove duplicates from a list.'''

# 1 method
list_1 = [1, 2, 1, 4, 6]
list_2=[1,2,3,4,5,6,7,8]
print(list(set(list_1)^set(list_2)))


# 2 method
list_value1=[12,15,11,12,8,15,3,3]  
print("The initialized list is ",list_value1)  
res_list=[]  
for i in list_value1:  
    if i not in res_list:  
        res_list.append(i)  
#printing the list after removing duplicate elements  
print("The resultant list after removing duplicates is ",res_list)  
