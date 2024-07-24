# 📘 Day 11
## 📌 Today's Progress
# Functions

'''Functions
So far we have seen many built-in Python functions. In this section, we will focus on custom functions. What is a function? Before we start making functions, let us learn what a function is and why we need them?

Defining a Function
A function is a reusable block of code or programming statements designed to perform a certain task. To define or declare a function, Python provides the def keyword. The following is the syntax for defining a function. The function block of code is executed only if the function is called or invoked.

Declaring and Calling a Function
When we make a function, we call it declaring a function. When we start using the it, we call it calling or invoking a function. Function can be declared with or without parameters.

# syntax
# Declaring a function
def function_name():
    codes
    codes
# Calling a function
function_name()
Function without Parameters
Function can be declared without parameters.

Example:

def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # calling a function

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()
Function Returning a Value - Part 1
Function can also return values, if a function does not have a return statement, the value of the function is None. Let us rewrite the above functions using return. From now on, we get a value from a function when we call the function and print it.

def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())
Function with Parameters
In a function we can pass different data types(number, string, boolean, list, tuple, dictionary or set) as a parameter

Single Parameter: If our function takes a parameter we should call our function with an argument
  # syntax
  # Declaring a function
  def function_name(parameter):
    codes
    codes
  # Calling function
  print(function_name(argument))
Example:

def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Asabeneh'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
Two Parameter: A function may or may not have a parameter or parameters. A function may also have two or more parameters. If our function takes parameters we should call it with arguments. Let us check a function with two parameters:
  # syntax
  # Declaring a function
  def function_name(para1, para2):
    codes
    codes
  # Calling function
  print(function_name(arg1, arg2))
Example:

def generate_full_name (first_name, last_name):
    space = ' '
      full_name = first_name + space + last_name
      return full_name
print('Full Name: ', generate_full_name('Asabeneh','Yetayeh'))

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;

print('Age: ', calculate_age(2021, 1819))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to a string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))
Passing Arguments with Key and Value
If we pass the arguments with key and value, the order of the arguments does not matter.

# syntax
# Declaring a function
def function_name(para1, para2):
    codes
    codes
# Calling function
print(function_name(para1 = 'John', para2 = 'Doe')) # the order of arguments does not matter here
Example:

def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print(print_fullname(firstname = 'Asabeneh', lastname = 'Yetayeh'))

def add_two_numbers (num1, num2):
    total = num1 + num2
    print(total)
print(add_two_numbers(num2 = 3, num1 = 2)) # Order does not matter
Function Returning a Value - Part 2
If we do not return a value with a function, then our function is returning None by default. To return a value with a function we use the keyword return followed by the variable we are returning. We can return any kind of data types from a function.

Returning a string: Example:
def print_name(firstname):
    return firstname
print_name('Asabeneh') # Asabeneh

def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    return full_name
print_full_name(firstname='Asabeneh', lastname='Yetayeh')
Returning a number:
Example:

def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(2, 3))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;
print('Age: ', calculate_age(2019, 1819))
Returning a boolean: Example:
def is_even (n):
    if n % 2 == 0:
        print('even')
        return True    # return stops further execution of the function, similar to break 
    return False
print(is_even(10)) # True
print(is_even(7)) # False
Returning a list: Example:
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))
Function with Default Parameters
Sometimes we pass default values to parameters, when we invoke the function. If we do not pass arguments when calling the function, their default values will be used.

# syntax
# Declaring a function
def function_name(param = value):
    codes
    codes
# Calling function
function_name()
function_name(arg)
Example:

def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Asabeneh'))

def generate_full_name (first_name = 'Asabeneh', last_name = 'Yetayeh'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('David','Smith'))

def calculate_age (birth_year,current_year = 2021):
    age = current_year - birth_year
    return age;
print('Age: ', calculate_age(1821))

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - average gravity on Earth's surface
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # gravity on the surface of the Moon
Arbitrary Number of Arguments
If we do not know the number of arguments we pass to our function, we can create a function which can take arbitrary number of arguments by adding * before the parameter name.

# syntax
# Declaring a function
def function_name(*args):
    codes
    codes
# Calling function
function_name(param1, param2, param3,..)
Example:

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total
print(sum_all_nums(2, 3, 5)) # 10
Default and Arbitrary Number of Parameters in Functions
def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
print(generate_groups('Team-1','Asabeneh','Brook','David','Eyob'))
Function as a Parameter of Another Function
#You can pass functions around as parameters
def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27
'''



# 💻 Exercises: Day 11

# Exercises: Level 1

#Function to add two numbers:
def add_two_numbers(a, b):
    return a + b

# Example usage
print(add_two_numbers(3, 5))  # Output: 8


# Function to calculate the area of a circle:
import math

def area_of_circle(r):
    return math.pi * r ** 2

# Example usage
print(area_of_circle(5))  # Output: 78.53981633974483

# Function to sum an arbitrary number of arguments:
def add_all_nums(*args):
    return sum(args)

# Example usage
print(add_all_nums(1, 2, 3, 4, 5))  # Output: 15


# Function to convert °C to °F:
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# Example usage
print(celsius_to_fahrenheit(0))  # Output: 32.0


# Function to check the season by month:
def check_season(month):
    seasons = {
        "December": "Winter", "January": "Winter", "February": "Winter",
        "March": "Spring", "April": "Spring", "May": "Spring",
        "June": "Summer", "July": "Summer", "August": "Summer",
        "September": "Autumn", "October": "Autumn", "November": "Autumn"
    }
    return seasons.get(month, "Invalid month")

# Example usage
print(check_season("March"))  # Output: Spring


# Function to calculate the slope of a linear equation:
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

# Example usage
print(calculate_slope(0, 0, 2, 2))  # Output: 1.0


# Function to solve a quadratic equation:
import math

def solve_quadratic_eqn(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return "No real solutions"
    elif discriminant == 0:
        return -b / (2 * a)
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2

# Example usage
print(solve_quadratic_eqn(1, -3, 2))  # Output: (2.0, 1.0)


# Function to print each element of a list:

def print_list(lst):
    for item in lst:
        print(item)

# Example usage
print_list([1, 2, 3, 4, 5])


# Function to reverse a list:

def reverse_list(lst):
    return lst[::-1]

# Example usage
print(reverse_list([1, 2, 3, 4, 5]))  # Output: [5, 4, 3, 2, 1]


# Function to capitalize each item in a list:

def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]

# Example usage
print(capitalize_list_items(["hello", "world"]))  # Output: ['Hello', 'World']


# Function to add an item to a list:
def add_item(lst, item):
    lst.append(item)
    return lst

# Example usage
print(add_item([1, 2, 3], 4))  # Output: [1, 2, 3, 4]


# Function to remove an item from a list:
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

# Example usage
print(remove_item([1, 2, 3, 4], 3))  # Output: [1, 2, 4]


# Function to sum all numbers in a range:

def sum_of_numbers(n):
    return sum(range(n + 1))

# Example usage
print(sum_of_numbers(10))  # Output: 55


# Function to sum all odd numbers in a range:

def sum_of_odds(n):
    return sum(i for i in range(n + 1) if i % 2 != 0)

# Example usage
print(sum_of_odds(10))  # Output: 25


# Function to sum all even numbers in a range:
def sum_of_even(n):
    return sum(i for i in range(n + 1) if i % 2 == 0)

# Example usage
print(sum_of_even(10))  # Output: 30



# Level 2 Exercises

# Function to count evens and odds:
def evens_and_odds(n):
    evens = len([i for i in range(n + 1) if i % 2 == 0])
    odds = n - evens + 1
    return {"evens": evens, "odds": odds}

# Example usage
print(evens_and_odds(10))  # Output: {'evens': 6, 'odds': 5}


# Function to calculate factorial:
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Example usage
print(factorial(5))  # Output: 120


# Function to check if a parameter is empty:
def is_empty(param):
    return not bool(param)

# Example usage
print(is_empty([]))  # Output: True
print(is_empty([1, 2, 3]))  # Output: False

# Functions to calculate mean, median, mode, range, variance, and standard deviation:
from statistics import mean, median, mode, variance, stdev

def calculate_mean(lst):
    return mean(lst)

def calculate_median(lst):
    return median(lst)

def calculate_mode(lst):
    return mode(lst)

def calculate_range(lst):
    return max(lst) - min(lst)

def calculate_variance(lst):
    return variance(lst)

def calculate_stdev(lst):
    return stdev(lst)

# Example usage
data = [1, 2, 2, 3, 4, 4, 4, 5]
print(calculate_mean(data))  # Output: 3.125
print(calculate_median(data))  # Output: 3.0
print(calculate_mode(data))  # Output: 4
print(calculate_range(data))  # Output: 4
print(calculate_variance(data))  # Output: 2.4107142857142856
print(calculate_stdev(data))  # Output: 1.5524174696260025


# Level 3 Exercises

# Function to check if a number is prime:
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage
print(is_prime(11))  # Output: True
print(is_prime(4))  # Output: False


# Function to check if all items in a list are unique:
def all_unique(lst):
    return len(lst) == len(set(lst))

# Example usage
print(all_unique([1, 2, 3, 4]))  # Output: True
print(all_unique([1, 2, 2, 4]))  # Output: False


# Function to check if all items in a list are of the same data type:
def same_data_type(lst):
    return all(isinstance(x, type(lst[0])) for x in lst)

# Example usage
print(same_data_type([1, 2, 3, 4]))  # Output: True
print(same_data_type([1, 2, "3", 4]))  # Output: False


# Function to check if a variable is a valid Python variable:
import keyword

def is_valid_variable(var):
    if var.isidentifier() and not keyword.iskeyword(var):
        return True
    return False

# Example usage
print(is_valid_variable("variable"))  # Output: True
print(is_valid_variable("123variable"))  # Output: False
print(is_valid_variable("for"))  # Output: False


# Function to return the most spoken languages:
def most_spoken_languages(n=10):
    languages = [
        "English", "Mandarin Chinese", "Hindi", "Spanish", "French", "Arabic", 
        "Bengali", "Russian", "Portuguese", "Urdu", "Indonesian", "German", 
        "Japanese", "Swahili", "Marathi", "Telugu", "Turkish", "Tamil", "Vietnamese", 
        "Korean"
    ]
    return languages[:n]

# Example usage
print(most_spoken_languages(10))  # Output: ['English', 'Mandarin Chinese', 'Hindi', 'Spanish', 'French', 'Arabic', 'Bengali', 'Russian', 'Portuguese', 'Urdu']


# Function to return the most populated countries:
def most_populated_countries(n=10):
    countries = [
        "China", "India", "United States", "Indonesia", "Pakistan", 
        "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico", 
        "Japan", "Ethiopia", "Philippines", "Egypt", "Vietnam", 
        "DR Congo", "Turkey", "Iran", "Germany", "Thailand"
    ]
    return countries[:n]

# Example usage
print(most_populated_countries(10))  # Output: ['China', 'India', 'United States', 'Indonesia', 'Pakistan', 'Brazil', 'Nigeria', 'Bangladesh', 'Russia', 'Mexico']


#

