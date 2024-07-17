# 💻 Exercises - Day 4

# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

string1 = 'Thirty'
string2 = 'Days'
string3 = 'Of'
string4 = 'Python'
concatenated_string1 = f"{string1} {string2} {string3} {string4}"
print(concatenated_string1)


# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
string1 = 'Coding'
string2 = 'For'
string3 = 'All'
concatenated_string2 = f"{string1} {string2} {string3}"
print(concatenated_string2)


# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"
print(company)


# 4. Print the variable company using print().
print(company)
print()


# 5. Print the length of the company string using len() method and print().
print(len(company))
print()
print()
print()


# 6 Change all the characters to uppercase letters using upper() method
print(company.upper())
print()


# 7. Change all the characters to lowercase letters using lower() method.
print(company.lower())


# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())
print()


# 9. Cut(slice) out the first word of Coding For All string.
print(company[0:6])
print()


# 10 . Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find("Coding"))
print()
print(company.index("Coding"))
print()
print(company.index("Coding", 0, 6))
print()
print(company.index("Coding", 0, 7))
print()
print(company.index("Coding", 0, 8))
print()
print(company.index("Coding", 0, 9))
print()
print(company.index("Coding", 0, 10))
print()
print(company.index("Coding", 0, 11))
print()


# 11. Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding", "Python"))
print()
print(company.replace("Coding", "Python", 1))
print()
print(company.replace("Coding", "Python", 2))
print()
print(company.replace("Coding", "Python", 3))
print()
print(company.replace("Coding", "Python", 4))
print()
print(company.replace("Coding", "Python", 5))
print()


# 12. Change Python for Everyone to Python for All using the replace method or other methods.
print(company.replace("Everyone", "All"))
print()
print(company.replace("Everyone", "All", 1))
print()


# 13. Split the string 'Coding For All' using space as the separator (split()) .
print(company.split(" "))
print()
print(company.split(" ", 1))
print()
print(company.split(" ", 2))


# 14 . "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
print(company.split(","))


# 15 . What is the character at index 0 in the string Coding For All.
print(company[0])
print()
print(company[0:1])
print()
print(company[0:2])
print()


# 16 . What is the last index of the string Coding For All.
print(company[-1])
print()
print(company[-2])
print()
print(company[-3])
print()
print(company[-4])  
print()


# 17 . What character is at index 10 in "Coding For All" string.
print(company[10])
print()
print(company[11])
print()
print(company[12])
print()


# 18 . Create an acronym or an abbreviation for the name 'Python For Everyone'.
phrase2 = 'Python For Everyone'
acronym1 = ''.join([word[0] for word in phrase2.split()])
print(acronym1)


# 19 . Create an acronym or an abbreviation for the name 'Coding For All'.
phrase3 = 'Coding For All'
acronym2 = ''.join([word[0] for word in phrase3.split()])
print(acronym2)


# 20 . Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))


# 21 . Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('F'))


# 22 . Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rfind('l'))


# 23 . Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))
print(sentence.find('because'))
print()
print(sentence.index('because', 1))
print(sentence.find('because', 1))
print()
print(sentence.index('because', 2))
print(sentence.find('because', 2))
print()


# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))
print()
print(sentence.rindex('because', 1))
print()
print(sentence.rindex('because', 2))
print()
print(sentence.rindex('because', 3))
print()


# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence[sentence.index('because'):sentence.rindex('because') + len('because')])
print()
print(sentence[sentence.index('because'):sentence.rindex('because') + len('because') +
               sentence[sentence.index('because'):sentence.rindex('because') + len('because')].
               index('because') + len('because')])
print()


# 26.  Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
print()
print(sentence.find('because', 1))
print()
print(sentence.find('because', 2))
print()
print(sentence.find('because', 3))
print()


# 27 . Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence[sentence.find('because'):sentence.find('because') + len('because')])
print()
print(sentence[sentence.find('because'):sentence.find('because') + len('because') +
               sentence[sentence.find('because'):sentence.find('because') + len('because')].
               find('because') + len('because')])
print()


# 28. Does ''Coding For All' start with a substring Coding?
sentence = 'Coding For All'
print(sentence.startswith('Coding'))
print()
print(sentence.startswith('Coding', 0))
print()
print(sentence.startswith('Coding', 1))
print()
print(sentence.startswith('Coding', 2))
print()


# 29. Does 'Coding For All' end with a substring coding?
sentence = 'Coding For All'
print(sentence.endswith('coding'))
print()
print(sentence.endswith('coding', 0))
print()
print(sentence.endswith('coding', 1))
print()
print(sentence.endswith('coding', 2))
print()


# 30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
sentence = '   Coding For All      '
print(sentence.strip())
print()
print(sentence.lstrip())
print()
print(sentence.rstrip())
print()
print(sentence.strip().lstrip().rstrip())
print()
print(sentence.strip().lstrip().rstrip().strip())
print()
print(sentence.strip().lstrip().rstrip().strip().strip())   
print()



''' 31. Which one of the following variables return True when we use the method isidentifier():
30DaysOfPython
thirty_days_of_python'''
print('30DaysOfPython'.isidentifier())
print()
print('thirty_days_of_python'.isidentifier())
print()
print('30DaysOfPython30'.isidentifier())
print()


# 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libraries = ' # '.join(python_libraries)
print(joined_libraries)


''' 33. Use the new line escape sequence to separate the following sentences.
I am enjoying this challenge.
I just wonder what is next.'''
print('I am enjoying this challenge.\nI just wonder what is next.')
print()


'''34. Use a tab escape sequence to write the following lines.
Name      Age     Country   City
Shantel  22     Kenya   Nairobi'''
print('Name\tAge\tCountry\tCity')
print('Shantel\t22\tKenya\tNairobi')

'''Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.'''
radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area} meters square.')
print()



'''Make the following using string formatting methods:
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144'''
print(f'8 + 6 = {8 + 6}')
print(f'8 - 6 = {8 - 6}')
print(f'8 * 6 = {8 * 6}')
print(f'8 / 6 = {8 / 6}')
print(f'8 % 6 = {8 % 6}')
print(f'8 // 6 = {8 // 6}')
print(f'8 ** 6 = {8 ** 6}')
print()



