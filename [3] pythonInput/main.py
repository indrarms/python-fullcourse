# Input() = A function that prompts the user for input and returns it as a string.
# In Python, input() is used to get user input. It takes an optional argument, which is a string that will be displayed as a prompt to the user.

# input() # Ouput: (waits for user input) and returns the input as a string.

# name = input("What is your name?: ")
# age = input("What is your age?: ")
# age = int(age) # Convert the age from a string to an integer.
# age += 1 # Increment the age by 1 to represent the next year.

# print(f"Hello, {name}!") # Output: Hello, [name]! (where [name] is the inputted name)
# print(f"Happy Birthday!")
# print(f"You are {age} years old.") # Output: You are [age] years old. (where [age] is the incremented age)

# or you can combine the input and print statements like this:
# name = input("What is your name?: ")
# age = int(input("What is your age?: ")) # Combines the input and conversion to integer in one line.
# age += 1

# print(f"Hello, {name}!")
# print(f"Happy Birthday!")
# print(f"You are {age} years old.")

# Excersice #1 : Rectangle Area Calculator

# length = float(input("Enter the length of the rectangle: ")) # Combines the input and conversion to float in one line.
# widht = float(input("Enter the width of the rectangle: "))
# area = length * widht

# print(f"The area of the rectangle is: {area}cm²") # Output: The area of the rectangle is: [area]cm² (where [area] is the calculated area)

# Excersice #2 : Shopping Cart Program
item = input("Enter the name of the item: ")
price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity of the item: "))
total_cost = price * quantity

print(f"You have added {quantity} x {item}/s) to your cart.")
print(f"Your total cost is ${total_cost}")