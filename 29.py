'''Write a Python program to unzip a list of tuples into individual lists.'''


data_list = [('Harry', 17), ('Hermione', 17), ('Ginny', 16)]

print('Original List: ', str(data_list))

unzipped_list = list(zip(*data_list))

print('Unzipped list', unzipped_list)
