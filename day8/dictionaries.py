# 📘 Day 8

# Dictionaries
# Dictionaries are a collection of key-value pairs.
# Dictionaries are written with curly brackets, and have keys and values separated by colons.
# You can access values by referring to their key name, within square brackets.
# Dictionaries are changeable, and values can be of any data type.
# A dictionary is a collection which is ordered, changeable, and does not allow duplicates.
#A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type


#💻 Exercises: Day 8

# 1. Create an empty dictionary called dog
dog = {}
print(dog)

# 2. Add name, color, breed, legs, age to the dog dictionary
dog = {
    "name": "Buddy",
    "color": "brown",
    "breed": "Golden Retriever",
    "legs": 4,
    "age": 3
}
print(dog)

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    "first_name": "John",
    "last_name": "Doe",
    "gender": "Male",
    "age": 25,
    "marital_status": "Single",
    "skills": ["Python", "Java", "C++"],
    "country": "Kenya",
    "city": "Lagos",
    "address": {
        "street": "No 1, Lagos Street",
        "zipcode": "12345"
    }
}
print(student)

# 4. Get the length of the student dictionary
print(len(student))

# 5. Get the value of skills and check the data type, it should be a list
skills = student['skills']
print(skills)
print(type(skills))

# 6. Modify the skills values by adding one or two skills
student['skills'].append("C#")
print(student['skills'])
student['skills'].append("JavaScript")
print(student['skills'])
print(student)

# 7. Get the dictionary keys as a list
keys = list(student.keys())
print(keys)
print(type(keys))

# 8. Get the dictionary values as a list
values = list(student.values())
print(values)
print(type(values))

# 9. Change the dictionary to a list of tuples using items() method
student_items = list(student.items())
print(student_items)
print(type(student_items))

# 10. Delete one of the items in the dictionary
del student['age']
print(student)

# 11. Delete one of the dictionaries
del student
# This line will raise a NameError because student is deleted
# print(student)  # Uncommenting this will cause an error
