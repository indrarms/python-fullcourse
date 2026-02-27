# This is a simple Python program that demonstrates basic print statements.

print("I love Python programming!")
print("Python is a versatile language that can be used for web development, data analysis, artificial intelligence, and more.")

# Varible = A container for storing data values (string, integer, float, boolean)
# In Python, you don't need to declare the type of variable, it is dynamically typed.
# A variable behaves as if it was the value that it contains.

# String = A sequence of characters enclosed in quotes (single, double, or triple quotes)
# In Python, strings are immutable, meaning that once a string is created, it cannot be changed. However, you can create new strings by concatenating or slicing existing ones.

first_name = "Candil"
food = "Pizza"
email = "candil@cendol.com"

print(f"Hello, my name is {first_name}.")
print(f"I like to eat {food}.")
print(f"My email is {email}.")

# Integer = A whole number without a decimal point
# In Python, integers can be of arbitrary size, meaning they can grow as needed to accommodate larger values.

age = 21
quantitiy = 10
num_of_students = 30

print(f"I am {age} years old.")
print(f"I have {quantitiy} items in my cart.")
print(f"There are {num_of_students} students in the class.")

# Float = A number with a decimal point
# In Python, floats are implemented using double-precision (64-bit) format, which provides a wide range of values and precision. However, it's important to note that floating-point arithmetic can sometimes lead to precision issues due to the way numbers are represented in binary.

price = 19.99
gpa = 3.5
distance = 5.75

print(f"The price of the item is ${price}.")
print(f"My GPA is {gpa}.")
print(f"The distance to the destination is {distance} miles.")

# Boolean = A data type that can only be True or False
# In Python, the boolean values are represented by the built-in constants True and False. They are often used in conditional statements and logical operations to control the flow of a program.

is_student = False
for_sale = True
is_online = True

print(f"Is the person a student? {is_student}.")
if is_student:
    print("The person is a student.")
else:
    print("The person is not a student.")

if for_sale:
    print("The item is for sale.")
else:
    print("The item is not for sale.")

if is_online:
    print("My friend is online.")
else:
    print("My friend is offline.")

# Task: Create a variable for each data type and print them out in a formatted string.
user_name = "Candil"
year = 2026
pi = 3.14
is_admin = True

print(f"User Name: {user_name}")
print(f"Year: {year}")
print(f"Pi: {pi}")
print(f"Is Admin: {is_admin}")