# Exercises: Day 6

####  Exercises: Level 1

# 1. Create an empty tuple
empty_tuple = ()
print(empty_tuple)


# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('Caroline', 'Mercy', 'Brandon')
brothers = ('Maloso', 'Issa', 'Mj')
siblings = sisters + brothers
print(siblings)


# 3. Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print(siblings)


# 4. How many siblings do you have?
print(len(siblings))


# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ('Awino', 'Brandon')
print(family_members)


###### Exercises: Level 2 #######


# 1. Unpack siblings and parents from family_members
siblings = family_members[:-2]
parents = family_members[-2:]
print(siblings)
print(parents)


# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple', 'banana', 'cherry')
vegetables = ('carrot', 'potato', 'tomato')
animal_products = ('milk', 'cheese', 'yoghurt')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)


# 3. Change the food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)


# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_index = len(food_stuff_lt) // 2
if len(food_stuff_lt) % 2 == 0:
    middle_items = food_stuff_lt[middle_index - 1:middle_index + 1]
else:
    middle_items = [food_stuff_lt[middle_index]]
print(middle_items)


# 5. Slice out the first three items and the last three items from food_stuff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print(first_three)
print(last_three)


# 6. Delete the food_stuff_tp tuple completely
del food_stuff_tp
try:
    print(food_stuff_tp)
except NameError:
    print("food_stuff_tp is deleted")


# 7. Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
is_estonia_nordic = 'Estonia' in nordic_countries
print(is_estonia_nordic)

is_iceland_nordic = 'Iceland' in nordic_countries
print(is_iceland_nordic)
