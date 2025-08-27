# 🐍 Python Refresher

> A concise Python refresher for developers with experience in other languages 🚀

This guide is for programmers who already know the basics of programming and want a fast overview of **Python’s syntax and essential features**. Use it to prepare for interviews, start a new project, or quickly transition from another language.

---

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
- Use `sort()` to arrange the list in ascending or descending order.
- Use `len()` to get the number of elements in a list.
```python
my_list.sort()
print(my_list)  # Output: [1, 2, 3, 4, 5]

my_list.sort(reverse=True)
print(my_list)  # Output: [5, 4, 3, 2, 1]

print(len(my_list))  # Output: 5
```

## Sets in Python

Sets are similar to lists but are **unordered collections** that do **not allow duplicate elements**. Sets are defined using curly braces `{}`.

```python
my_set = {1, 2, 5, 9, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5, 9}
# Note: Duplicate '5' is removed and order is not guaranteed.
```

**Looping Through a Set:**
```python
for item in my_set:
    print(item)
```

**Adding Elements:**
- Use `add()` to insert a single element.
- Use `update()` to add multiple elements.

```python
my_set.add(7)
print(my_set)  # Output: {1, 2, 3, 4, 5, 7, 9}

my_set.update([6, 8, 10])
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
```

**Removing Elements:**
- `remove(item)` deletes an element but raises an error if the element is not found.
- `discard(item)` deletes an element if present, but does nothing if not found.

```python
my_set.remove(10)
# my_set.remove(11)  # Raises KeyError if uncommented

my_set.discard(9)
my_set.discard(11)  # No error if 11 is not present
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
```

**Clearing a Set:**
- Clear all
```python
my_set.clear()
print(my_set)  # Output: set()
```

## Tuples in Python

Tuples are ordered, immutable collections of items.  
They are defined using parentheses `()`.

```python
my_tuple = (1, 2, 2, 6, 3, 4, 5)
print(my_tuple)  # Output: (1, 2, 2, 6, 3, 4, 5)
```

**Immutability:**  
Tuples cannot be changed after creation.

```python
my_tuple[0] = 10  # Raises TypeError
```

**Accessing Elements:**  
Access tuple elements by index.

```python
print(my_tuple[0])  # Output: 1
```

**Unchangeable Nature:**  
You cannot add, remove, or modify items in a tuple after it is created.

**Tuple Packing and Unpacking:**

```python
# Packing
person = ("Alice", 30, "Engineer")

# Unpacking
name, age, profession = person
print(name)       # Output: Alice
print(age)        # Output: 30
print(profession) # Output: Engineer
```

## Assignment-03: List Assignment

**Task:**  
- Create a list of 5 animals called `zoo`
- Delete the animal at the 3rd index
- Append a new animal at the end of the list
- Delete the animal at the beginning of the list
- Print all the animals
- Print only the first 3 animals

**Solution:**
```python
zoo = ["Lion", "Tiger", "Elephant", "Giraffe", "Zebra"]

# Delete the animal at the 3rd index
zoo.pop(3)
print(zoo)  # Output: ['Lion', 'Tiger', 'Elephant', 'Zebra']

# Append a new animal at the end of the list
zoo.append("Deer")
print(zoo)  # Output: ['Lion', 'Tiger', 'Elephant', 'Zebra', 'Deer']

# Delete the animal at the beginning of the list
zoo.pop(0)
print(zoo)  # Output: ['Tiger', 'Elephant', 'Zebra', 'Deer']

# Print all the animals
for animal in zoo:
    print(animal)  # Output: 'Tiger', 'Elephant', 'Zebra', 'Deer'

# Print only the first 3 animals
print(zoo[:3]) #print(zoo[0:3]) # Output: ['Tiger', 'Elephant', 'Zebra']
```

## Booleans and Operators in Python

**Boolean Type:**  
Booleans represent truth values: `True` or `False`.

```python
is_liked = True
print(type(is_liked))  # Output: <class 'bool'>
```

**Comparison Operators:**  
Used to compare values.

```python
print(1 == 1)   # Equal: True
print(1 != 1)   # Not equal: False
print(1 > 2)    # Greater than: False
print(2 >= 1)   # Greater than or equal: True
print(1 < 5)    # Less than: True
print(1 <= 7)   # Less than or equal: True
```

**Logical Operators:**  
Combine multiple conditions.

```python
print(2 > 1 and 5 < 7)    # Both must be True: True
print(2 >= 1 or 5 < 7)    # At least one is True: True
print(not(1 == 1))        # Negates the condition: False
```

## Flow Control: If, Elif, Else

Python uses indentation to define blocks of code for flow control statements.

**If Statement:**
```python
age = 1
if age < 3:
    print("Baby")  # Output: Baby
```

**If-Else Statement:**
```python
is_boy = False
if is_boy:
    print("Boy")
else:
    print("Girl")  # Output: Girl
```

**Elif (Else If):**
```python
hour = 16
if hour < 12:
    print("Good Morning")
elif hour >= 12 and hour <= 17:
    print("Good Afternoon")  # Output: Good Afternoon
else:
    print("Good Evening")
```

## Assignment-04: If-Else Assignment

**Task:**  
- Create a variable `grade` holding an integer between 0 - 100.
- Use if, elif, else statements to print the letter grade based on the number grade.

**Grades:**
- A = 90 - 100
- B = 80 - 89
- C = 70 - 79
- D = 60 - 69
- F = 0 - 59

**Solution:**
```python
grade = 87
if grade >= 90 and grade <= 100:
    print("A")
elif 80 <= grade <= 89:  # If two variables are the same, you can write "80 <= grade <= 89"
    print("B")
elif 70 <= grade <= 79:
    print("C")
elif 60 <= grade <= 69:
    print("D")
else:
    print("F")
```
```