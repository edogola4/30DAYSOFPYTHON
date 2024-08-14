# 📘 Day 21

# Classes and Objects

'''Python is an object oriented programming language. Everything in Python is an object, with its properties and methods. A number, string, list, dictionary, tuple, set etc. used in a program is an object of a corresponding built-in class. We create class to create an object. A class is like an object constructor, or a "blueprint" for creating objects. We instantiate a class to create an object. The class defines attributes and the behavior of the object, while the object, on the other hand, represents the class.

We have been working with classes and objects right from the beginning of this challenge unknowingly. Every element in a Python program is an object of a class. Let us check if everything in python is a class:

asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> num = 10
>>> type(num)
<class 'int'>
>>> string = 'string'
>>> type(string)
<class 'str'>
>>> boolean = True
>>> type(boolean)
<class 'bool'>
>>> lst = []
>>> type(lst)
<class 'list'>
>>> tpl = ()
>>> type(tpl)
<class 'tuple'>
>>> set1 = set()
>>> type(set1)
<class 'set'>
>>> dct = {}
>>> type(dct)
<class 'dict'>
Creating a Class
To create a class we need the key word class followed by the name and colon. Class name should be CamelCase.

# syntax
class ClassName:
  code goes here
Example:

class Person:
  pass
print(Person)
<__main__.Person object at 0x10804e510>
Creating an Object
We can create an object by calling the class.

p = Person()
print(p)
Class Constructor
In the examples above, we have created an object from the Person class. However, a class without a constructor is not really useful in real applications. Let us use constructor function to make our class more useful. Like the constructor function in Java or JavaScript, Python has also a built-in init() constructor function. The init constructor function has self parameter which is a reference to the current instance of the class Examples:

class Person:
      def __init__ (self, name):
        # self allows to attach parameter to the class
          self.name =name

p = Person('Asabeneh')
print(p.name)
print(p)
# output
Asabeneh
<__main__.Person object at 0x2abf46907e80>
Let us add more parameters to the constructor function.

class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city


p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)
# output
Asabeneh
Yetayeh
250
Finland
Helsinki
Object Methods
Objects can have methods. The methods are functions which belong to the object.

Example:

class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'

p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.person_info())
# output
Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland
Object Default Methods
Sometimes, you may want to have a default values for your object methods. If we give default values for the parameters in the constructor, we can avoid errors when we call or instantiate our class without parameters. Let's see how it looks:

Example:

class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

p1 = Person()
print(p1.person_info())
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
# output
Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland.
John Doe is 30 years old. He lives in Noman city, Nomanland.
Method to Modify Class Default Values
In the example below, the person class, all the constructor parameters have default values. In addition to that, we have skills parameter, which we can access using a method. Let us create add_skill method to add skills to the skills list.

class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
          self.skills = []

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
      def add_skill(self, skill):
          self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
print(p1.skills)
print(p2.skills)
# output
Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland.
John Doe is 30 years old. He lives in Noman city, Nomanland.
['HTML', 'CSS', 'JavaScript']
[]
Inheritance
Using inheritance we can reuse parent class code. Inheritance allows us to define a class that inherits all the methods and properties from parent class. The parent class or super or base class is the class which gives all the methods and properties. Child class is the class that inherits from another or parent class. Let us create a student class by inheriting from person class.

class Student(Person):
    pass


s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)
output
Eyob Yetayeh is 30 years old. He lives in Helsinki, Finland.
['JavaScript', 'React', 'Python']
Lidiya Teklemariam is 28 years old. He lives in Espoo, Finland.
['Organizing', 'Marketing', 'Digital Marketing']
We did not call the init() constructor in the child class. If we didn't call it then we can still access all the properties from the parent. But if we do call the constructor we can access the parent properties by calling super.
We can add a new method to the child or we can override the parent class methods by creating the same method name in the child class. When we add the init() function, the child class will no longer inherit the parent's init() function.

Overriding parent method
class Student(Person):
    def __init__ (self, firstname='Asabeneh', lastname='Yetayeh',age=250, country='Finland', city='Helsinki', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname,age, country, city)
    def person_info(self):
        gender = 'He' if self.gender =='male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki','male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)
Eyob Yetayeh is 30 years old. He lives in Helsinki, Finland.
['JavaScript', 'React', 'Python']
Lidiya Teklemariam is 28 years old. She lives in Espoo, Finland.
['Organizing', 'Marketing', 'Digital Marketing']
We can use super() built-in function or the parent name Person to automatically inherit the methods and properties from its parent. In the example above we override the parent method. The child method has a different feature, it can identify, if the gender is male or female and assign the proper pronoun(He/She).'''



# 💻 Exercises: Day 21

# Exercises: Level 1

# 1. Python has the module called statistics and we can use this module to do all the statistical calculations. However, to learn how to make function and reuse function let us try to develop a program, which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. Check the output below.
'''ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range() # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]'''


# solution 
from collections import Counter
import math

class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return self.sum() / self.count()

    def median(self):
        sorted_data = sorted(self.data)
        n = self.count()
        middle = n // 2
        if n % 2 == 0:
            return (sorted_data[middle - 1] + sorted_data[middle]) / 2
        else:
            return sorted_data[middle]

    def mode(self):
        frequency = Counter(self.data)
        most_common = frequency.most_common(1)[0]
        return most_common

    def variance(self):
        mean = self.mean()
        return sum((x - mean) ** 2 for x in self.data) / self.count()

    def std(self):
        return math.sqrt(self.variance())

    def freq_dist(self):
        frequency = Counter(self.data)
        return sorted([(freq / self.count(), value) for value, freq in frequency.items()], reverse=True)

    def describe(self):
        return {
            'Count': self.count(),
            'Sum': self.sum(),
            'Min': self.min(),
            'Max': self.max(),
            'Range': self.range(),
            'Mean': self.mean(),
            'Median': self.median(),
            'Mode': self.mode(),
            'Variance': self.variance(),
            'Standard Deviation': self.std(),
            'Frequency Distribution': self.freq_dist(),
        }

# Example usage:
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)
print(data.describe())


# Exercises: Level 2

# 2. Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for expenses.

class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []

    def add_income(self, amount, description):
        self.incomes.append({'amount': amount, 'description': description})

    def add_expense(self, amount, description):
        self.expenses.append({'amount': amount, 'description': description})

    def total_income(self):
        return sum(item['amount'] for item in self.incomes)

    def total_expense(self):
        return sum(item['amount'] for item in self.expenses)

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        return {
            'Firstname': self.firstname,
            'Lastname': self.lastname,
            'Total Income': self.total_income(),
            'Total Expense': self.total_expense(),
            'Account Balance': self.account_balance(),
        }

# Example usage:
person = PersonAccount('Shantel', 'Shartel')
person.add_income(5000, 'Salary')
person.add_income(200, 'Freelance')
person.add_expense(1500, 'Rent')
person.add_expense(200, 'Groceries')

print(person.account_info())


#  Basic Class Manipulation

'''Class for Books:
Create a Book class with the following attributes: title, author, year, and genre. Include methods to:

Display the book's details.
Check if the book was published in the current century (year >= 2000).'''

class Books: 
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def display_info(self):
        return f"'{self.title}' by {self.author} ({self.year}) - Genre: {self.genre}"
    
    def is_current_century(self):
        return self.year >= 2000

# Example Usage:
book = Books('The Road', 'Brandon McOgola', 2006, 'Dystopian')
print(book.display_info())
print('Published in the current century:', book.is_current_century())


# Class for Bank Account:

'''Create a BankAccount class with account_number, account_holder, balance attributes. Add methods to:

Deposit money.
Withdraw money (check if the balance is sufficient before withdrawing).
Display the current balance.'''


class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance +=amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance -= amount
        return self.balance
    
    def display_balance(self):
        return f"Account {self.account_number} balance: ksh{self.balance}"
    
# Example Usage:
account = BankAccount('123456789', 'Brandon McOgola', 1000000000)
account.deposit(50000000)
print(account.withdraw(1000000))
print(account.display_balance())



# Class for Library:
'''Build a Library class that manages a collection of books. The class should:

Add a book to the collection.
Remove a book by title.
Display all books in the library.
Search for books by a particular author.'''

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        self.books = [book for book in self.books if book.title != title]

    def display_books(self):
        if not self.books:
            return "No books in the library."
        return '\n'.join(book.display_info() for book in self.books)
    
    def search_by_author(self, author):
        results = [book for book in self.books if book.author == author]
        if not results:
            return f"No books found by {author}. "
        return '\n'.join(book.display_info() for book in results)
    
# Example Usage
library = Library()
book1 = Books('The Road', 'Brandon McOgola', 2006, 'Dystopian')
book2 = Books('1984', 'George Orwel', 1949, "Dystopian")
library.add_book(book1)
library.add_book(book2)
print(library.display_books())
print(library.search_by_author('George orwel'))


# Class for Shopping Cart:
'''Create a ShoppingCart class that allows you to:

Add items to the cart (each item has a name, price, and quantity).
Remove items from the cart.
Calculate the total cost.
Display all items in the cart.'''

class ShoppingCart:
    def __init__(self) :
        self.items = []

    def add_item(self,name, price, quantity=1):
        self.items.append({'name': name, 'price': price, 'quantity':quantity})

    def remove_item(self, name):
        self.items = [item for item in self.items if item['name'] != name]

    def total_cost(self):
        return sum(item['price'] * item['quantity'] for item in self.items)
    
    def display_cart(self):
        if not self.items:
            return "Your cart is empty."
        return '\n'.join(f"{item['quantity']} * {item['name']} @ KSH{item['price']} each" for item in self.items)
    
# Example Usage:
cart = ShoppingCart()
cart.add_item('Apple', 0.5, 10)
cart.add_item('Banana', 0.2, 5)
print (cart.display_cart())
print('Total cost:', cart.total_cost())
cart.remove_item('Banana')
print(cart.display_cart())




# Advanced Class Features

'''Class for School Management System:
Design a School class that manages students and teachers. Each Person in the school should have a name and an ID. The school should:

Add a student or teacher to the system.
Remove a student or teacher by ID.
Display all students and teachers.
Search for a person by name.'''

class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display_info(self):
        return f"{self.name} (ID: {self.id})"

class School:
    def __init__(self):
        self.students = []
        self.teachers = []

    def add_person(self, person, role):
        if role == 'student':
            self.students.append(person)
        elif role == 'teacher':
            self.teachers.append(person)

    def remove_person(self, id, role):
        if role == 'student':
            self.students = [student for student in self.students if student.id != id]
        elif role == 'teacher':
            self.teachers = [teacher for teacher in self.teachers if teacher.id != id]

    def display_people(self, role):
        if role == 'student':
            if not self.students:
                return "No students found."
            return '\n'.join(student.display_info() for student in self.students)
        elif role == 'teacher':
            if not self.teachers:
                return "No teachers found."
            return '\n'.join(teacher.display_info() for teacher in self.teachers)

    def search_person(self, name):
        results = [person for person in self.students + self.teachers if person.name == name]
        if not results:
            return f"No person found with the name {name}."
        return '\n'.join(person.display_info() for person in results)

# Example usage:
school = School()
student1 = Person('Shartel', 1)
student2 = Person('McOgola', 2)
teacher1 = Person('Mr. Smith', 101)
school.add_person(student1, 'student')
school.add_person(student2, 'student')
school.add_person(teacher1, 'teacher')
print(school.display_people('student'))
print(school.display_people('teacher'))
print(school.search_person('Shartel'))



# Class for Online Store:

'''Create a class OnlineStore that manages products and customer orders. The class should:

Add products (each product has a name, price, and stock quantity).
Place an order (check if the requested quantity is available).
Display all products.
Track order history for each customer.
'''

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_product(self):
        return f"{self.name}: ${self.price} ({self.quantity} in stock)"

class OnlineStore:
    def __init__(self):
        self.products = []
        self.orders = {}

    def add_product(self, product):
        self.products.append(product)

    def place_order(self, customer_name, product_name, quantity):
        product = next((p for p in self.products if p.name == product_name), None)
        if not product:
            return "Product not found."
        if product.quantity < quantity:
            return "Not enough stock available."
        product.quantity -= quantity
        if customer_name not in self.orders:
            self.orders[customer_name] = []
        self.orders[customer_name].append({'product': product_name, 'quantity': quantity})
        return f"Order placed for {quantity}x {product_name}"

    def display_products(self):
        return '\n'.join(product.display_product() for product in self.products)

    def display_orders(self, customer_name):
        if customer_name not in self.orders:
            return f"No orders found for {customer_name}."
        return '\n'.join(f"{order['quantity']}x {order['product']}" for order in self.orders[customer_name])

# Example usage:
store = OnlineStore()
product1 = Product('Laptop', 1000, 5)
product2 = Product('Phone', 500, 10)
store.add_product(product1)
store.add_product(product2)
print(store.display_products())
print(store.place_order('Shantel', 'Laptop', 2))
print(store.display_orders(''))
