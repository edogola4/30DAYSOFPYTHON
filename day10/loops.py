'''
📘 Day 10
Loops
Life is full of routines. In programming we also do lots of repetitive tasks. In order to handle repetitive task programming languages use loops. Python programming language also provides the following types of two loops:

while loop
for loop
While Loop
We use the reserved word while to make a while loop. It is used to execute a block of statements repeatedly until a given condition is satisfied. When the condition becomes false, the lines of code after the loop will be continued to be executed.

  # syntax
while condition:
    code goes here
Example:

count = 0
while count < 5:
    print(count)
    count = count + 1
#prints from 0 to 4
In the above while loop, the condition becomes false when count is 5. That is when the loop stops. If we are interested to run block of code once the condition is no longer true, we can use else.

  # syntax
while condition:
    code goes here
else:
    code goes here
Example:

count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
The above loop condition will be false when count is 5 and the loop stops, and execution starts the else statement. As a result 5 will be printed.

Break and Continue - Part 1
Break: We use break when we like to get out of or stop the loop.
# syntax
while condition:
    code goes here
    if another_condition:
        break
Example:

count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
The above while loop only prints 0, 1, 2, but when it reaches 3 it stops.

Continue: With the continue statement we can skip the current iteration, and continue with the next:
  # syntax
while condition:
    code goes here
    if another_condition:
        continue
Example:

count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1
The above while loop only prints 0, 1, 2 and 4 (skips 3).

For Loop
A for keyword is used to make a for loop, similar with other programming languages, but with some syntax differences. Loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

For loop with list
# syntax
for iterator in lst:
    code goes here
Example:

numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5
For loop with string
# syntax
for iterator in string:
    code goes here
Example:

language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])
For loop with tuple
# syntax
for iterator in tpl:
    code goes here
Example:

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
For loop with dictionary Looping through a dictionary gives you the key of the dictionary.
  # syntax
for iterator in dct:
    code goes here
Example:

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out
Loops in set
# syntax
for iterator in st:
    code goes here
Example:

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)
Break and Continue - Part 2
Short reminder: Break: We use break when we like to stop our loop before it is completed.

# syntax
for iterator in sequence:
    code goes here
    if condition:
        break
Example:

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break
In the above example, the loop stops when it reaches 3.

Continue: We use continue when we like to skip some of the steps in the iteration of the loop.

  # syntax
for iterator in sequence:
    code goes here
    if condition:
        continue
Example:

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')
In the example above, if the number equals 3, the step after the condition (but inside the loop) is skipped and the execution of the loop continues if there are any iterations left.

The Range Function
The range() function is used list of numbers. The range(start, end, step) takes three parameters: starting, ending and increment. By default it starts from 0 and the increment is 1. The range sequence needs at least 1 argument (end). Creating sequences using range

lst = list(range(11)) 
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}
# syntax
for iterator in range(start, end, step):
Example:

for number in range(11):
    print(number)   # prints 0 to 10, not including 11
Nested For Loop
We can write loops inside a loop.

# syntax
for x in y:
    for t in x:
        print(t)
Example:

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)
For Else
If we want to execute some message when the loop ends, we use else.

# syntax
for iterator in range(start, end, step):
    do something
else:
    print('The loop ended')
Example:

for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)
Pass
In python when statement is required (after semicolon), but we don't like to execute any code there, we can write the word pass to avoid errors. Also we can use it as a placeholder, for future statements.

Example:

for number in range(6):
    pass

'''

# 💻 Exercises: Day 10
# Exercises: Level 1

# 1. Iterate 0 to 10 using for loop, do the same using while loop.
for i in range(11):
    print(i)

#while
i = 0
while i < 11:
    print(i)
    i += 1

# 2. Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(10, -1, -1):
    print(i)
    #while
    i = 10
    while i >= 0:
        print(i)
        i -= 1


# 3. 
'''Write a loop that makes seven calls to print(), so we get on the output the following triangle:

  #
  ##
  ###
  ####
  #####
  ######
  #######'''
for i in range(1, 8):
    print(i * '#')
    

# 4. 
'''Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #'''
for i in range(7):
    for j in range(7):
        print('#', end='')
        print()



# 5. 
'''Print the following pattern:

0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100'''
for i in range(10):
    print(i, 'x', i, '=', i * i)



# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
list = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in list:
    print(i)


# 7. Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(0, 101):
    if i % 2 == 0:
        print(i)


# 8. Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(0, 101):
    if i % 2 != 0:
        print(i)


        #Exercises: Level 2

# 1. 
'''Use for loop to iterate from 0 to 100 and print the sum of all numbers.
The sum of all numbers is 5050.'''
sum = 0
for i in range(0, 101):
    sum += i
    print(sum)

# 2. 
'''Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

The sum of all evens is 2550. And the sum of all odds is 2500.'''
sum = 0
for i in range(0, 101):
    if i % 2 == 0:
        sum += i
        print(sum)
    else:
       sum += i
print(sum)


# Exercises: Level 3#######

# 1.
'''Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.'''
countries = ["Finland", "Iceland", "Thailand", "Switzerland", "Ireland", "Netherlands", "New Zealand"]
land_countries = [country for country in countries if 'land' in country]
print(land_countries)


# 2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
for i in range(len(fruits)-1, -1, -1):
    print(fruits[i])


# 3. 
'''Go to the data folder and use the countries_data.py file.
What are the total number of languages in the data
Find the ten most spoken languages from the data
Find the 10 most populated countries in the world'''


# i
countries_data = [
    {"name": "Finland", "languages": ["Finnish", "Swedish"]},
    {"name": "Sweden", "languages": ["Swedish"]},
    {"name": "Norway", "languages": ["Norwegian"]},
    {"name": "Denmark", "languages": ["Danish"]},
    {"name": "Iceland", "languages": ["Icelandic"]}
]
unique_languages = set()
for country in countries_data:
    for language in country["languages"]:
        unique_languages.add(language)
print(f"Total number of languages: {len(unique_languages)}")


# ii 
from collections import Counter

language_counter = Counter()
for country in countries_data:
    language_counter.update(country["languages"])

most_spoken_languages = language_counter.most_common(10)
print(most_spoken_languages)

# iii 
countries_data = [
    {"name": "China", "population": 1409517397},
    {"name": "India", "population": 1339180127},
    {"name": "USA", "population": 324459463},
    {"name": "Indonesia", "population": 263991379},
    {"name": "Brazil", "population": 209288278},
    {"name": "Pakistan", "population": 197015955},
    {"name": "Nigeria", "population": 190886311},
    {"name": "Bangladesh", "population": 164669751},
    {"name": "Russia", "population": 143989754},
    {"name": "Mexico", "population": 129163276}
]
most_populated_countries = sorted(countries_data, key=lambda x: x["population"], reverse=True)[:10]
print(most_populated_countries)


