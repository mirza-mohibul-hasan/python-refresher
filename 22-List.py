# Lists are collection of data as like arrays in other programming languages.

my_list = [2, 5, 3, 4, 1]

people_list = ["Alice", "Bob", "Charlie", "David"]

mixed_list = [1, "Hello", 3.14, True]

# Index is always zero-based.
print(mixed_list[0])  # Output: 1
print(mixed_list[1])  # Output: Hello
print(mixed_list[2])  # Output: 3.14
print(mixed_list[3])  # Output: True

# Slicing
print(mixed_list[1:3])  # Output: ['Hello', 3.14]
#  Here we get a sublist from index 1 to 3 (excluding 3)

# Append
mixed_list.append("New Item")
print(mixed_list)  # Output: [1, "Hello", 3.14, True, "New Item"]

# Insert
mixed_list.insert(2, "Inserted Item")
print(mixed_list)  # Output: [1, "Hello", "Inserted Item", 3.14, True, "New Item"]

# Remove
mixed_list.remove("Hello")
print(mixed_list)  # Output: [1, "Inserted Item", 3.14, True, "New Item"]

# Pop
popped_item = mixed_list.pop()
print(popped_item)  # Output: New Item
print(mixed_list)  # Output: [1, "Inserted Item", 3.14, True]

mixed_list.pop(1)
print(mixed_list)  # Output: [1, 3.14, True]

# Sort
my_list.sort()
print(my_list)  # Output: [1, 2, 3, 4, 5]

my_list.sort(reverse=True)
print(my_list)  # Output: [5, 4, 3, 2, 1]

# len
print(len(my_list))  # Output: 5

