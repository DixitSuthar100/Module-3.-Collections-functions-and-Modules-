'''Write a Python program to remove an empty tuple(s) from a list of tuples.'''

list = [(), ('ram','15','8'), (), ('laxman', 'sita'),
          ('krishna', 'akbar', '45'), ('',''),()]
for tuple in list:
    if(len(tuple)==0):
        list.remove(tuple)
print(list)
