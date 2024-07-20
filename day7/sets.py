# python Sets
# 💻 Exercises: Day 7

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1

# 1. Find the length of the set it_companies
print('Length of it_companies:', len(it_companies))

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print('it_companies after adding Twitter:', it_companies)

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['Intel', 'SAP', 'Salesforce'])
print('it_companies after adding multiple companies:', it_companies)

# 4. Remove one of the companies from the set it_companies
it_companies.remove('Twitter')
print('it_companies after removing Twitter:', it_companies)

# 5. What is the difference between remove and discard
# remove: removes the element if it exists in the set
# discard: removes the element if it exists in the set, but does not raise an error if
# the element does not exist in the set

# Exercises: Level 2

# 1. Join A and B
print('A:', A)
print('B:', B)
union = A.union(B)
print('Union of A and B:', union)

# 2. Find A intersection B
intersection = A.intersection(B)
print('Intersection of A and B:', intersection)

# 3. Is A a subset of B
is_subset = A.issubset(B)
print("Is A a subset of B:", is_subset)

# 4. Are A and B disjoint sets
are_disjoint = A.isdisjoint(B)
print("Are A and B disjoint sets:", are_disjoint)

# 5. Join A with B and B with A
union_A_B = A.union(B)
union_B_A = B.union(A)
print('Union of A with B:', union_A_B)
print('Union of B with A:', union_B_A)

# 6. Symmetric difference between A and B
sym_diff = A.symmetric_difference(B)
print('Symmetric difference between A and B:', sym_diff)

# 7. Delete the sets completely
del A
del B
try:
    print('A:', A)
except NameError:
    print('A has been deleted.')
try:
    print('B:', B)
except NameError:
    print('B has been deleted.')

# Exercises: Level 3

# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages_set = set(age)
print('Length of the list:', len(age))
print('Length of the set:', len(ages_set))
if len(age) > len(ages_set):
    print('The list is bigger than the set.')
else:
    print('The set is bigger than the list.')

# 2. Explain the difference between the following data types: string, list, tuple and set
# String: A sequence of characters. It is immutable.
# List: An ordered collection of items. It is mutable.
# Tuple: An ordered collection of items. It is immutable.
# Set: An unordered collection of unique items. It is mutable.

# 3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people.'
words = sentence.split()
unique_words = set(words)
print('Number of unique words:', len(unique_words))
print('Unique words:', unique_words)

#### 🎉 CONGRATULATIONS ! 🎉 ######
