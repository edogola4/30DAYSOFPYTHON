'''By default, statements in Python script are executed sequentially from top to bottom. If the processing logic require so, the sequential flow of execution can be altered in two way:

Conditional execution: a block of one or more statements will be executed if a certain expression is true
Repetitive execution: a block of one or more statements will be repetitively executed as long as a certain expression is true. In this section, we will cover if, else, elif statements. The comparison and logical operators we learned in previous sections will be useful here.'''
# if statement
# if statement is used to execute a block of code if a certain condition is true.
# The syntax of if statement is:
# if condition:
#     statement(s)
# The condition after if statement is evaluated. If the condition is true, the statement is executed.
# If the condition is false, the statement is skipped.
# Example:
# Write a program to check if a number is positive or negative.
# If the number is positive, print "Positive".
# If the number is negative, print "Negative".
# If the number is zero, print "Zero".
# number = 5
# if number > 0:
#     print("Positive")
# number = -5
# if number < 0:
#     print("Negative")
# number = 0
# if number == 0:
#     print("Zero")
# The above program will produce the following result.
# Positive
# Negative
# Zero
# Note: The statement after if statement is executed only if the condition is true. If the condition
# is false, the statement is skipped.
# Example:
# Write a program to check if a number is positive or negative.
# If the number is positive, print "Positive".
# If the number is negative, print "Negative".
# If the number is zero, print "Zero".
# number = 5
# if number > 0:
#     print("Positive")
# number = -5
# if number < 0:
#     print("Negative")
# number = 0
# if number == 0:
#     print("Zero")
# The above program will produce the following result.
# Positive
# Negative
# Zero
# Note: The statement after if statement is executed only if the condition is true. If the condition
# is false, the statement is skipped.



# 💻 Exercises: Day 9
# Level 1
# Exercise 1
'''Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.'''
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are old enough to drive.")
# else:
#     print("You need", 18 - age, "more years to learn to drive.")
# Output:
# Enter your age: 30
# You are old enough to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.

age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to drive.")
else:
    print("You need", 18 - age, "more years to learn to drive.")



# 2. 
'''Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
Enter your age: 30
You are 5 years older than me.'''

my_age = 24
your_age = int(input("Enter your age: "))

if my_age > your_age:
    difference = your_age - my_age
    year_text = "year" if difference == 1 else "years"
    print(f"You are {difference} {year_text} older than me.")

elif your_age < my_age:
    difference = my_age - your_age
    year_text = "year" if difference == 1 else "years"
    print(f"I am {difference} {year_text} older than you.")

else:
    print("We are the same age.")


# 3 . 
'''Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
Enter number one: 4
Enter number two: 3
4 is greater than 3'''

a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")



###### Level 2 #####
# 1.
'''Write a code which gives grade to students according to theirs scores:

80-100, A
70-89, B
60-69, C
50-59, D
0-49, F'''

score = int(input("Enter your score: "))

if 80 <= score <= 100:
    grade = 'A'
elif 70 <= score < 80:
    grade = 'B'
elif 60 <= score < 70:
    grade = 'C'
elif 50 <= score < 60:
     grade = 'D'
else:
     grade = 'F'
print(f"Your grade is {grade}")


# 2. 
'''Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer'''
season = input("Enter the month: ")
if season == "September" or season == "October" or season == "November":
    print("Autumn")
elif season == "December" or season == "January" or season == "February":
    print("Winter")
elif season == "March" or season == "April" or season == "May":
    print("Spring")
elif season == "June" or season == "July" or season == "August":
    print("Summer")
else:
    print("Wrong input")


# 3 
'''The following list contains some fruits:

fruits = ['banana', 'orange', 'mango', 'lemon']
If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')'''

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter the fruit: ")

if fruit in fruits:
    print("That fruit already exist in the list")
else:
  fruits.append(fruit)
print("Updated fruits list: ", fruits)


##### level 3#####

#1. 
'''Here we have a person dictionary. Feel free to modify it!

        person={
    'first_name': 'Edwin',
    'last_name': 'Ogola',
    'age': 24,
    'country': 'Kenya',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
 * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:
    Asabeneh Yetayeh lives in Finland. He is married.'''
person = {
    'first_name': 'Edwin',
    'last_name': 'Ogola',
    'age': 24,
    'country': 'Kenya',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
        }
}
if 'skills' in person:
    print(person['skills'][1])
    if 'skills' in person:
        if 'Python' in person['skills']:
            print('He has Python skill')
            if 'skills' in person:
                if 'JavaScript' in person['skills'] and 'React' in person['skills']:
                    print('He is a front end developer')
                elif 'Node' in person['skills'] and 'Python' in person['skills'] and'MongoDB' in person['skills']:
                  print('He is a backend developer')
elif 'React' in person['skills'] and 'Node' in person['skills'] and'MongoDB' in person['skills']:
  print('He is a fullstack developer')
else:
  print('unknown title')
if 'is_marred' in person and person['is_marred'] == True and 'country' in person and person['country'] == 'Finland':
 print(person['first_name'] + ' ' + person['last_name'] + ' lives in '
      + person['country'] + '. He is married.')
