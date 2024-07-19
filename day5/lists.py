# Exercises: Level 1

# 1. Declare an empty list
empty_list = []
print(empty_list)

# 2. Declare a list with more than 5 items
item_list = [1, 2, 3, 4, 5, 6]
print(item_list)

# 3. Find the length of your list
length_of_list = len(item_list)
print(length_of_list)

# 4. Get the first item, the middle item and the last item of the list
first_item = item_list[0]
middle_item = item_list[len(item_list) // 2]
last_item = item_list[-1]
print(first_item, middle_item, last_item)

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Shantel", 22, 5.8, "dating", "123 Nairobi"]
print(mixed_data_types)

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)

# 7. Print the list using print()
print(it_companies)

# 8. Print the number of companies in the list
print(len(it_companies))

# 9. Print the first, middle and last company
print(it_companies[0])
print(it_companies[len(it_companies) // 2])
print(it_companies[-1])

# 10. Print the list after modifying one of the companies
it_companies[0] = "Facebook Inc"
print(it_companies)

# 11. Add an IT company to it_companies
it_companies.append("Microsoft Inc")
print(it_companies)
print(len(it_companies))

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(2, "Google Inc")
print(it_companies)

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()
print(it_companies)

# 14. Join the it_companies with a string '#;  '
it_companies_str = "#;  ".join(it_companies)
print(it_companies_str)

# 15. Check if a certain company exists in the it_companies list.
company_exists = "Google" in it_companies
print(company_exists)

# 16. Sort the list using sort() method
it_companies.sort()
print(it_companies)

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# 18. Slice out the first 3 companies from the list
first_three = it_companies[:3]
print(first_three)

# 19. Slice out the last 3 companies from the list
last_three = it_companies[-3:]
print(last_three)

# 20. Slice out the middle IT company or companies from the list
middle = it_companies[len(it_companies) // 2 - 1:len(it_companies) // 2 + 1]
print(middle)

# 21. Remove the first IT company from the list
del it_companies[0]
print(it_companies)

# 22. Remove the middle IT company or companies from the list
middle_index = len(it_companies) // 2
del it_companies[middle_index]
print(it_companies)

# 23. Remove the last IT company from the list
del it_companies[-1]
print(it_companies)

# 24. Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# 25. Destroy the IT companies list
del it_companies

# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

joined_list = front_end + back_end
print(joined_list)

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = joined_list.copy()
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')
print(full_stack)

##### Exercises: Level 2 #####

# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# a. Sort the list and find the min and max age
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print("Sorted ages:", ages)
print("Min age:", min_age)
print("Max age:", max_age)

# b. Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
print(ages)

# c. Find the median age (one middle item or two middle items divided by two)
middle_index = len(ages) // 2
if len(ages) % 2 == 0:
    median_age = (ages[middle_index - 1] + ages[middle_index]) / 2
else:
    median_age = ages[middle_index]
print("Median age:", median_age)

# d. Find the average age (sum of all items divided by their number)
average_age = sum(ages) / len(ages)
print("Average age:", average_age)

# e. Find the range of the ages (max minus min)
age_range = max_age - min_age
print("Age range:", age_range)

# f. Compare the value of (min - average) and (max - average), use abs() method
min_average_diff = abs(min_age - average_age)
max_average_diff = abs(max_age - average_age)
print("Difference between min age and average age:", min_average_diff)
print("Difference between max age and average age:", max_average_diff)

# g. Find the middle country(ies) in the countries list
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
middle_index = len(countries) // 2
if len(countries) % 2 == 0:
    middle_countries = countries[middle_index - 1: middle_index + 1]
else:
    middle_countries = [countries[middle_index]]
print("Middle country(ies):", middle_countries)

# h. Divide the countries list into two equal lists if it is even if not one more country for the first half.
half_index = (len(countries) + 1) // 2
first_half = countries[:half_index]
second_half = countries[half_index:]
print("First half:", first_half)
print("Second half:", second_half)

# i. Unpack the first three countries and the rest as scandic countries.
china, russia, usa, *scandic_countries = countries
print("First three countries:", china, russia, usa)
print("Scandic countries:", scandic_countries)
