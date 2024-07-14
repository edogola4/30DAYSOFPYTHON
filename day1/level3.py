#Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.


# Number
integer_num = 10            # Integer
float_num = 9.8             # Float
complex_num = 4 - 4j        # Complex

# String
string_example = "Hello, Python!"

# Boolean
boolean_example = True
boolean_example = False

# List
list_example = [1, 2, 3, 4, 5]

# Tuple
tuple_example = (1, 2, 3, 4, 5)

# Set
set_example = {1, 2, 3, 4, 5}

# Dictionary
dict_example = {'name': 'Shantel', 'age': 22, 'country': 'Kenya', 'county': 'migori', 'sub-county': 'uriri'}
print(dict_example) #simple print statement

for key, value in dict_example.items():
    print(f"{key}: {value}") #iterating and printing each key-value pair


import json
print(json.dumps(dict_example, indent=4)) #converting dictionary to json format


#Find an Euclidian distance between (2, 3) and (10, 8)


import math

x1 = 2
y1 = 3
x2 = 10
y2 = 8

#calculate distance
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(distance)