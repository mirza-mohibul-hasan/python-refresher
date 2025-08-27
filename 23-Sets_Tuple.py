""" 
Sets are similar to lists but they are unordered and do not allow duplicate elements.
Use curly braces {} to create a set.
Set automatically sorts the elements on creation.
"""

my_set = {1, 2, 5, 9, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5, 9} - Note that the duplicate '5' is removed and order is not guaranteed.

# we can loop through a set
for item in my_set:
    print(item)
    
# insert into set
my_set.add(7)
print(my_set)  # Output: {1, 2, 3, 4, 5, 7, 9}

# insert multiple elements
my_set.update([6, 8, 10])
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# remove from set
""" 
remove() function raises error if element not found
"""
my_set.remove(10)
my_set.remove(11)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

""" 
discard() function does not raise error if element not found
"""
my_set.discard(9)
my_set.discard(11)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}


# clear the set
my_set.clear()
print(my_set)  # Output: set()

""" 
Tuples are ordered, immutable collections of items.
They are defined using parentheses ().
"""

my_tuple = (1, 2, 2, 6, 3, 4, 5)
print(my_tuple)  # Output: (1, 2, 2, 6, 3, 4, 5)

# immutable characteristics
my_tuple[0] = 10  # This will raise a TypeError

# Accessing elements
print(my_tuple[0])  # Output: 1

# Inserting elements
""" Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
 """