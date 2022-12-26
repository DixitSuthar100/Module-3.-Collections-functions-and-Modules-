'''Write a Python program to map two lists into a dictionary'''

#1.method

keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
color_dictionary = dict(zip(keys, values))
print(color_dictionary)


#2.method

test_keys = ["Rash", "Kil", "Varsha"]
test_values = [1, 4, 5]
 
# Printing original keys-value lists
print("Original key list is : " + str(test_keys))
print("Original value list is : " + str(test_values))
 
# to convert lists to dictionary
res = {}
for key in test_keys:
    for value in test_values:
        res[key] = value
        test_values.remove(value)
        break
print("Resultant dictionary is : " + str(res))
