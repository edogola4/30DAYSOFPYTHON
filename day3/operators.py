#### OPERATORS  ###


import math

# Declare your age as integer variable
age = 24
print(age)

# Declare your height as a float variable
height = 6.34
print(height)

# Declare a variable that store a complex number
complex_number = 3 + 4j
print(complex_number)

# Prompt the user to enter base and height of the triangle and calculate its area
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height
print(f"The area of the triangle is {area}")

# Prompt the user to enter sides of the triangle and calculate its perimeter
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))
perimeter = side_a + side_b + side_c
print(f"The perimeter of the triangle is {perimeter}")

# Get length and width of a rectangle using prompt. Calculate its area and perimeter
length = float(input("Enter length: "))   
width = float(input("Enter width: "))
area = length * width
perimeter = 2 * (length + width)
print(f"The area of the rectangle is {area}")
print(f"The perimeter of the rectangle is {perimeter}")

# Get radius of a circle using prompt. Calculate the area and circumference
radius = float(input("Enter radius: "))
pi = 3.14
area = pi * radius * radius
circumference = 2 * pi * radius
print(f"The area of the circle is {area}")
print(f"The circumference of the circle is {circumference}")

# Calculate the slope, x-intercept and y-intercept of y = 2x - 2
slope = 2
x_intercept = -1 * (-2/slope)
y_intercept = -2
print(f"Slope = {slope}")
print(f"x-intercept = {x_intercept}")
print(f"y-intercept = {y_intercept}")

# Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1) / (x2 - x1)
euclidean_distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Slope = {slope}")
print(f"Euclidean distance = {euclidean_distance}")

# Compare the slopes
slope_8 = 2
slope_9 = slope
print(f"The slopes are the same: {slope_8 == slope_9}")

# Calculate the value of y = x^2 + 6x + 9 and figure out when y is 0
x = -3
y = x**2 + 6*x + 9
print(f"y = 0 when x = {x}")
print(f"y = {y}")

# Find the length of 'python' and 'dragon' and make a falsy comparison statement
length_python = len("python")
length_dragon = len("dragon")
print(f"Length of python = {length_python}")
print(f"Length of dragon = {length_dragon}")
print(f"False comparison statement = {length_python > length_dragon}")

# Use 'and' operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

# Check if 'jargon' is in the sentence
sentence = "I hope this course is not full of jargon."
print('jargon' in sentence)

# There is no 'on' in both 'dragon' and 'python'
print('on' not in 'python' and 'on' not in 'dragon')

# Find the length of the text python and convert the value to float and string
length_python = len("python")
float_python = float(length_python)
string_python = str(float_python)
print(f"Length of python = {length_python}")
print(f"Float value of python = {float_python}")
print(f"String value of python = {string_python}")

# Check if a number is even
number = int(input("Enter number to check if it is even: "))
print(f"{number} is even: {number % 2 == 0}")
print(f"{number} is odd: {number % 2 != 0}")

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
print(7 // 3 == int(2.7))

# Check if type of '10' is equal to type of 10
print(f"type of '10' = {type('10')}")
print(f"type of 10 = {type(10)}")
print(f"type of '10' is not equal to type of 10 = {type('10') != type(10)}")

# Check if int(float('9.8')) is equal to 10
try:
    print(int(float('9.8')) == 10)
except ValueError:
    print("Cannot convert '9.8' to an integer")

# Calculate weekly earnings
hours = float(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))
weekly_earning = hours * rate_per_hour
print(f"Your weekly earning is {weekly_earning}")

# Calculate the number of seconds a person can live
years_lived = int(input("Enter number of years you have lived: "))
seconds_lived = years_lived * 365 * 24 * 60 * 60
print(f"You have lived for {seconds_lived} seconds")

# Display the following table
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")
