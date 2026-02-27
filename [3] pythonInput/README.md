# Python User Input

The `input()` function is used to receive data from the user during program execution. When the program reaches `input()`, it pauses and waits for the user to enter a value.

---

### The String Rule

`input()` always returns data as a string (`str`), regardless of what the user types.

If the program requires numerical operations, explicit typecasting must be applied using functions such as `int()` or `float()`.

---

### Why Typecasting Is Necessary

Since mathematical operations cannot be performed directly on strings, user input must be converted to the appropriate numeric data type before calculations. Failing to convert input will either cause errors or produce unintended results (such as string concatenation instead of arithmetic addition).

---

## Exercises

---

### 1. Rectangle Area Calculator

This exercise focuses on calculating the area of a rectangle using user-provided dimensions.

**Objective:**

* Accept length and width as input.
* Convert both values to floating-point numbers using `float()` to ensure decimal precision.
* Multiply length by width using the formula:

```
area = length * width
```

**Key Concepts Practiced:**

* Using `input()` for numeric values
* Converting string input to `float`
* Performing arithmetic operations
* Displaying output using formatted strings

This exercise reinforces the importance of proper typecasting when working with decimal numbers.

---

### 2. Shopping Cart Program

This exercise simulates a simple shopping cart calculation.

**Objective:**

* Accept an item name as a string.
* Accept the item price as a floating-point number using `float()`.
* Accept the quantity as an integer using `int()`.
* Calculate the total cost:

```
total = price * quantity
```

**Key Concepts Practiced:**

* Handling multiple user inputs with different data types
* Using `float()` for monetary values
* Using `int()` for countable quantities
* Performing arithmetic calculations
* Formatting output clearly using f-strings

This exercise emphasizes correct data type selection and demonstrates how improper casting could lead to calculation errors.

---

### Important Considerations

* Always convert user input before performing mathematical operations.
* Use `type(variable)` to verify data types when debugging.
* Ensure that numeric conversions are valid to avoid `ValueError` exceptions.
* Choose `float()` when precision is required and `int()` for whole-number quantities.
