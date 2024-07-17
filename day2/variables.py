# Day 2: 30 Days of Python Programming
# Variables

# Exercise: 1

# Declare a first name variable and assign a value to it
first_name = "Shantel"
print(first_name)

# Declare a last name variable and assign a value to it
last_name = "Atieno"
print(last_name)

#Declare a middle name variable and assign a value to it
middle_name = "Odhiambo"
print(middle_name)

# Declare a full name variable and assign a value to it
full__name = first_name + "" + last_name + "" + middle_name
print(full__name)

# Declare a country variable and assign a value to it
country = "Kenya"
print(country)

# Declare a city variable and assign a value to it
city = "Nairobi"
print(city)

# Declare an age variable and assign a value to it
age = 22
print(age)

# Declare a year variable and assign a value to it
year = 2002
print(year)

# Declare a variable is_married and assign a value to it
is_married = False
print(is_married)


#Declare a variable is_true and assign a value to it
is_true = True
print(is_true)


# Declare a variable is_light_on and assign a value to it
is_light_on = False
print(is_light_on)



# Declare multiple variable on one line
a, b , c = 1, 2, 3
print(a)



# Exercise 2

# Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(middle_name))
print(type(full__name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(a))
print(type(b))
print(type(c))
#print(type(a, b, c))


# Using the len() built-in function, find the length of your first name
print(len(first_name))

# Compare the length of your first name and your last name
print(len(first_name) > len(last_name))
print(len(first_name) < len(last_name))
print(len(first_name) == len(last_name))
print(len(first_name) != len(last_name))

''' Declare 5 as num_one and 4 as num_two
a) Add num_one and num_two and assign the value to a variable total
b) Subtract num_two from num_one and assign the value to a variable diff
c) Multiply num_two and num_one and assign the value to a variable product
d) Divide num_one by num_two and assign the value to a variable division
e) Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
f) Calculate num_one to the power of num_two and assign the value to a variable exp
g) Find floor division of num_one by num_two and assign the value to a variable floor_division'''
 
num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

print("Total", total)
print("Difference", diff)
print("Product", product)
print("Division", division)
print("Remainder", remainder)
print("Exponent", exp)
print("Floor Division", floor_division)


''' The radius of a circle is 30 meters.
a) Calculate the area of a circle and assign the value to a variable name of area_of_circle
b) Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
c) Take radius as user input and calculate the area.'''

radius = 30
area_of_circle = 3.14 * radius ** 2
circum_of_circle = 2 * 3.14 * radius

print("Area of circle", area_of_circle)
print("Circumference of circle", circum_of_circle)

radius = int(input("Enter radius: "))
area_of_circle = 3.14 * radius ** 2
print("Area of circle", area_of_circle)


# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
country = input("Enter country: ")
age = int(input("Enter age: "))
print("First name", first_name)
print("Last name", last_name)
print("Country", country)
print("Age", age)


# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
import keyword
help("keywords")

# Use the built-in input function to get a word from a user and store the value to a variable name of word.
# Check if the word is a Python keyword or not. If it is a keyword, print "The word is a keyword".
# If it is not a keyword, print "The word is not a keyword".
word = input("Enter a word: ")

if word in keyword.kwlist:
    print("The word is a keyword")
else:
    print("The word is not a keyword")



