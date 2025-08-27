## Built-in Data Types in Python

| Category       | Data Types                              |
|----------------|----------------------------------------|
| Text Type      | `str`                                  |
| Numeric Types  | `int`, `float`, `complex`              |
| Sequence Types | `list`, `tuple`, `range`               |
| Mapping Type   | `dict`                                 |
| Set Types      | `set`, `frozenset`                     |
| Boolean Type   | `bool`                                 |
| Binary Types   | `bytes`, `bytearray`, `memoryview`     |
| None Type      | `NoneType`                             |

## Numeric Variables in Python

**Integers and Floats:**  
Python supports numeric variables like integers (`int`) and floating-point numbers (`float`).

```python
cost = 10           # integer
tax_percent = 0.25  # float
tax = cost * tax_percent
price = cost + tax
print(price)        # Output: 12.5
```

## Assignment-01

**Task:**  
Write a Python program that simulates buying an item with tax and prints the remaining money.

**Instructions:**
- You have $50.
- You buy an item that costs $15 with a 3% tax.
- Print how much money you have left after the purchase.

**Solution:**
```python
wallet = 50
item_price = 15
tax_rate = 0.03
wallet -= item_price + (item_price * tax_rate)
print(wallet)  # Output: 34.55
```

## Strings in Python

**Single and Double Quotes:**  
Strings can be defined using either single (`'`) or double (`"`) quotes.

```python
username = "mirzaree"
first_name = 'Mohibul'
print(username + " " + first_name)  # Output: mirzaree Mohibul
```

## Comments in Python

**Single-line Comments:**  
Use `#` for single-line comments.

```python
# This is a single-line comment
print("Hello, World!")  # This prints a message
```

**Multi-line Comments (Docstrings):**  
Triple quotes (`'''` or `"""`) are used for multi-line comments or docstrings.

```python
"""
This is a multi-line comment (docstring).
It can span multiple lines.
"""
```

## String Formatting in Python

**F-Strings:**  
Introduced in Python 3.6, f-strings provide a concise way to embed expressions inside string literals.

```python
first_name = "John"
last_name = "Doe"
age = 30
print(f"Hello, my name is {first_name} {last_name} and I am {age} years old.")
# Output: Hello, my name is John Doe and I am 30 years old.
```

**str.format() Method:**  
The `str.format()` method allows you to insert values into a string using curly braces `{}` as placeholders.

```python
first_name = "John"
last_name = "Doe"
sentence = "Hi {} {}"
print(sentence.format(first_name, last_name))
# Output: Hi John Doe
```

## User Input in Python

**Getting Input from the User:**  
Use the `input()` function to prompt the user for input. The input is always returned as a string.

```python
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
```

**Type Casting Input:**  
If you expect a numeric value, convert the input string to an integer (or float) using `int()` or `float()`.

```python
age = int(age)  # Converts the input string to an integer
```

**Example:**
```python
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
age = int(age)  # Convert age to integer

print(f"Hello, {first_name} {last_name}. You are {age} years old.")
```
## Assignment-02: String Assignment

**Task:**  
Ask the user how many days until their birthday and print the approximate number of weeks and days left.

**Solution:**
```python
days_until_birthday = int(input("How many days until your birthday? "))

weeks_until = days_until_birthday // 7
rem_days = days_until_birthday % 7
print(f"There are approximately {weeks_until} weeks and {rem_days} days until your birthday.")

# "/"" is True division and "//"" Floor Division
```

## Lists in Python

Lists are collections of items, similar to arrays in other programming languages. Lists can store elements of different data types and are mutable (can be changed after creation).

```python
my_list = [2, 5, 3, 4, 1]

people_list = ["Alice", "Bob", "Charlie", "David"]

mixed_list = [1, "Hello", 3.14, True]
```

**Indexing:**  
List indices start at 0.

```python
print(mixed_list[0])  # Output: 1
print(mixed_list[1])  # Output: Hello
print(mixed_list[2])  # Output: 3.14
print(mixed_list[3])  # Output: True
```

**Slicing:**  
Get a sublist using slicing (`list[start:end+1]`).

```python
print(mixed_list[1:3])  # Output: ['Hello', 3.14]
```

**Adding Elements:**  
- `append()` adds to the end.
- `insert(index, item)` adds at a specific position.

```python
mixed_list.append("New Item")
print(mixed_list)  # Output: [1, "Hello", 3.14, True, "New Item"]

mixed_list.insert(2, "Inserted Item")
print(mixed_list)  # Output: [1, "Hello", "Inserted Item", 3.14, True, "New Item"]
```

**Removing Elements:**  
- `remove(item)` removes the first occurrence.
- `pop()` removes and returns the last item or item at a given index.

```python
mixed_list.remove("Hello")
print(mixed_list)  # Output: [1, "Inserted Item", 3.14, True, "New Item"]

popped_item = mixed_list.pop()
print(popped_item)  # Output: New Item
print(mixed_list)   # Output: [1, "Inserted Item", 3.14, True]

mixed_list.pop(1)
print(mixed_list)   # Output: [1, 3.14, True]
```

**Sorting and Length:**

```python
my_list.sort()
print(my_list)  # Output: [1, 2, 3, 4, 5]

my_list.sort(reverse=True)
print(my_list)  # Output: [5, 4, 3, 2, 1]

print(len(my_list))  # Output: 5
```