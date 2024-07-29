### 📘 Day 14 ###

### Higher Order Functions ###

'''In Python functions are treated as first class citizens, allowing you to perform the following operations on functions:

A function can take one or more functions as parameters
A function can be returned as a result of another function
A function can be modified
A function can be assigned to a variable
In this section, we will cover:

Handling functions as parameters
Returning functions as return value from another functions
Using Python closures and decorators
Function as a Parameter
def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<

def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15
Function as a Return Value
def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3
You can see from the above example that the higher order function is returning different functions depending on the passed parameter

Python Closures
Python allows a nested function to access the outer scope of the enclosing function. This is is known as a Closure. Let us have a look at how closures work in Python. In Python, closure is created by nesting a function inside another encapsulating function and then returning the inner function. See the example below.

Example:

def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20
Python Decorators
A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a function you want to decorate.

Creating Decorators
To create a decorator function, we need an outer function with an inner wrapper function.

Example:

# Normal function
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON

## Let us implement the example above with a decorator

### This decorator function is a higher order function
that takes a function as a parameter
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON
Applying Multiple Decorators to a Single Function
####These decorator functions are higher order functions
that take functions as parameters

# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string_decorator
@uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON
Accepting Parameters in Decorator Functions
Most of the time we need our functions to take parameters, so we might need to define a decorator that accepts parameters.

def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))

print_full_name("Asabeneh", "Yetayeh",'Finland')
Built-in Higher Order Functions
Some of the built-in higher order functions that we cover in this part are map(), filter, and reduce. Lambda function can be passed as a parameter and the best use case of lambda functions is in functions like map, filter and reduce.

Python - Map Function
The map() function is a built-in function that takes a function and iterable as parameters.

    # syntax
    map(function, iterable)
Example:1

numbers = [1, 2, 3, 4, 5] # iterable
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# Lets apply it with a lambda function
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
Example:2

numbers_str = ['1', '2', '3', '4', '5']  # iterable
numbers_int = map(int, numbers_str)
print(list(numbers_int))    # [1, 2, 3, 4, 5]
Example:3

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# Let us apply it with a lambda function
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']
What actually map does is iterating over a list. For instance, it changes the names to upper case and returns a new list.

Python - Filter Function
The filter() function calls the specified function which returns boolean for each item of the specified iterable (list). It filters the items that satisfy the filtering criteria.

    # syntax
    filter(function, iterable)
Example:1

# Lets filter only even nubers
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]
Example:2

numbers = [1, 2, 3, 4, 5]  # iterable

def is_odd(num):
    if num % 2 != 0:
        return True
    return False

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))       # [1, 3, 5]
# Filter long name
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable
def is_name_long(name):
    if len(name) > 7:
        return True
    return False

long_names = filter(is_name_long, names)
print(list(long_names))         # ['Asabeneh']
Python - Reduce Function
The reduce() function is defined in the functools module and we should import it from this module. Like map and filter it takes two parameters, a function and an iterable. However, it does not return another iterable, instead it returns a single value. Example:1

numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15'''



#### 💻 Exercises: Day 14 ####

'''countries = ['Kenya', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Shantel', 'Brandon', 'Issa', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]'''

# Exercises: Level 1

# 1. Explain the difference between map, filter, and reduce.

'''map: The map function applies a given function to each item in an iterable (such as a list) and returns a new iterable (usually a list) with the results.

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
# squared_numbers = [1, 4, 9, 16, 25]
filter: The filter function applies a given function to each item in an iterable and returns a new iterable containing only the items for which the function returns True.


numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# even_numbers = [2, 4]
reduce: The reduce function applies a given function to the items of an iterable, cumulatively, from left to right, to reduce the iterable to a single value. It’s part of the functools module.


from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
# sum_of_numbers = 15'''


# 2. Explain the difference between higher order function, closure and decorator

'''Higher Order Function: A higher-order function is a function that takes another function as an argument, or returns a function as a result.


def higher_order_function(f):
    def wrapper():
        print("Before function call")
        f()
        print("After function call")
    return wrapper
Closure: A closure is a function that remembers the values from its enclosing lexical scope even when the program flow is no longer in that scope.


def outer_function(text):
    def inner_function():
        print(text)
    return inner_function
closure_function = outer_function('Hello')
closure_function()  # prints 'Hello'
Decorator: A decorator is a special type of higher-order function used to modify the behavior of another function. Decorators are typically used in Python with the @decorator_name syntax.


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
say_hello()
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.'''




# 3. Define a call function before map, filter or reduce, see examples.
def add_one(x):
    return x + 1

numbers = [1, 2, 3, 4, 5]
new_numbers = list(map(add_one, numbers))
print(new_numbers)
# new_numbers = [2, 3, 4, 5, 6]


# 4. Use for loop to print each country in the countries list.

countries = ['Kenya', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
for country in countries:
    print(country)



# 5. Use for to print each name in the names list.
names = ['Alice', 'Bob', 'Charlie', 'Diana']
for name in names:
    print(name)



# 6. Use for to print each number in the numbers list.
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)



###### Exercises: Level 2 #####

# 1. Use map to create a new list by changing each country to uppercase in the countries list.
countries = ['Kenya', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
uppercase_countries = list(map(lambda country: country.upper(), countries))
print(uppercase_countries)



# 2. Use map to create a new list by changing each number to its square in the numbers list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda number: number ** 2, numbers))
print(squared_numbers)


# 3. Use map to change each name to uppercase in the names list
names = ['Alice', 'Bob', 'Charlie', 'Diana']
uppercase_names = list(map(lambda name: name.upper(), names))
print(uppercase_names)


# 4. Use filter to filter out countries containing 'land'
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
countries_without_land = list(filter(lambda country: 'land' not in country, countries))
print(countries_without_land)


# 5. Use filter to filter out countries having exactly six characters.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
countries_with_six_chars = list(filter(lambda country: len(country) == 6, countries))
print(countries_with_six_chars)
# Output: ['Sweden', 'Norway']


# 6. Use filter to filter out countries containing six letters and more in the country list.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
countries_with_six_or_more_letters = list(filter(lambda country: len(country) >= 6, countries))
print(countries_with_six_or_more_letters)
# Output: ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']



# 7. Use filter to filter out countries starting with an 'E'
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
countries_starting_with_e = list(filter(lambda country: country.startswith('E'), countries))
print(countries_starting_with_e)
# Output: ['Estonia']


# 8. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 0, map(lambda x: x**2, numbers)))
print(result)
# Output: 220 (2^2 + 4^2 + 6^2 + 8^2 + 10^2 = 4 + 16 + 36 + 64 + 100)



# 9. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.

def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))

mixed_list = [1, 'Hello', 3.5, 'World', True, 'Python']
string_list = get_string_lists(mixed_list)
print(string_list)
# Output: ['Hello', 'World', 'Python']


# 10. Use reduce to sum all the numbers in the numbers list.
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)
# Output: 15

# 11. Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
sentence = reduce(lambda x, y: x + ', ' + y, countries[:-1]) + ', and ' + countries[-1] + ' are north European countries.'
print(sentence)
# Output: "Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries."


# 12 . Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
def categorize_countries(pattern):
    return list(filter(lambda country: pattern in country, countries))

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland', 'India', 'Pakistan']
land_countries = categorize_countries('land')
print(land_countries)
# Output: ['Finland', 'Iceland']


# 13. Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
def country_dict(countries):
    from collections import defaultdict
    country_count = defaultdict(int)
    for country in countries:
        country_count[country[0]] += 1
    return dict(country_count)


# 14 . Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
def get_first_ten_countries(countries):
    return countries[:10]


# 15. Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries(countries):
    return countries[-10:]



####Exercises: Level 3 ####

# 1. 
'''Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
Sort countries by name, by capital, by population
Sort out the ten most spoken languages by location.
Sort out the ten most populated countries.'''

# Assuming you have a list of countries where each country is represented by a dictionary with 'name', 'capital', and 'population' keys
countries_data = [
    {'name': 'Estonia', 'capital': 'Tallinn', 'population': 1325648},
    # ... other countries
]

sorted_by_name = sorted(countries_data, key=lambda x: x['name'])
sorted_by_capital = sorted(countries_data, key=lambda x: x['capital'])
sorted_by_population = sorted(countries_data, key=lambda x: x['population'])


# Assuming you have a list of languages with their number of speakers
languages_data = [
    {'language': 'English', 'speakers': 1500},
    # ... other languages
]

top_ten_languages = sorted(languages_data, key=lambda x: x['speakers'], reverse=True)[:10]


top_ten_populated_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)[:10]


