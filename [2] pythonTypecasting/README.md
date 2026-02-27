# Python Typecasting

**Typecasting** is the process of converting a variable from one data type to another. In Python, this is essential for performing specific operations or displaying data in a certain format.

---

### Two Types of Typecasting

1. **Implicit (Automatic):** Python automatically converts one type to another (e.g., adding an `int` to a `float` results in a `float`).
2. **Explicit (Manual):** The programmer manually converts a variable using built-in functions.



---

### Built-in Conversion Functions

| Function | Purpose | Example |
| :--- | :--- | :--- |
| `int()` | Converts to an Integer | `int(3.5)` -> `3` |
| `float()` | Converts to a Floating point | `float(21)` -> `21.0` |
| `str()` | Converts to a String | `str(21)` -> `"21"` |
| `bool()` | Converts to a Boolean | `bool("Text")` -> `True` |

---

### Important Considerations

* **Compatibility:** Not all conversions are possible. Converting a non-numeric string (e.g., `"Hello"`) to an `int` will result in a `ValueError`.
* **User Input:** Python `input()` always returns a string. You must typecast it if you need to perform math (e.g., `age = int(input("Age: "))`).
* **The `type()` Function:** Always use `type(variable)` to verify the conversion was successful before and after casting.