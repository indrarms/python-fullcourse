# Typecastin = Converting one data type to another data type. In Python, typecasting is the process of converting a variable from one data type to another.
# This can be done using built-in functions such as int(), float(), str(), and bool().

# Typecasting is useful when you want to perform operations that require a specific data type or when you want to display data in a certain format.
# For example, user input is often received as a string, and you may need to typecast it to an integer or float to perform calculations. Always be cautious when typecasting to avoid errors or unintended consequences in your code.
# The type() function can be used to check the data type of a variable before and after typecasting to ensure that the conversion has been successful.
# In Python, typecasting can be implicit (automatic) or explicit (manual). Implicit typecasting occurs when Python automatically converts one data type to another during an operation, while explicit typecasting requires the programmer to manually convert a variable using the appropriate function.
# For example, when you add an integer and a float, Python will implicitly convert the integer to a float before performing the addition. However, if you want to convert a string to an integer, you would need to explicitly use the int() function.
# It's important to note that not all type conversions are possible. For instance, trying to convert a non-numeric string to an integer will result in a ValueError. Therefore, it's crucial to ensure that the data being typecasted is compatible with the target data type to avoid runtime errors in your code.


name = "Indra Ramdani Saputra"
age = 21
gpa = 3.5
is_student = True

# print(type(name))  # Output: <class 'str'>
# print(type(age))   # Output: <class 'int'>
# print(type(gpa))   # Output: <class 'float'>
# print(type(is_student))  # Output: <class 'bool'>

# gpa = int(gpa)  # Typecasting float to int
# print(gpa)  # Output: 3

# age = float(age)  # Typecasting int to float
# print(age)  # Output: 21.0

# age = str(age)  # Typecasting int to str
# age += "1"  # Concatenating string "1" to age, output will be "211" because age is now a string

# print(age)  # Output: "21"
# print(type(age))  # Output: <class 'str'>

name = bool(name)  # Typecasting str to bool, output will be True because name is not an empty string
print(name)  # Output: True