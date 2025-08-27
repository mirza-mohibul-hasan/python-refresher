""" 
- Create a list of 5 animals called zoo
- Delete the animal at the 3rd index.
- Append a new animal at the end of the list
- Delete the animal at the beginning of the list.
- Print all the animals
- Print only the first 3 animals
"""

zoo = ["Lion", "Tiger", "Elephant", "Giraffe", "Zebra"]

# Delete the animal at the 3rd index.
zoo.pop(3-1)
print(zoo) # Output: ['Lion', 'Tiger', 'Giraffe', 'Zebra']

# Append a new animal at the end of the list
zoo.append("Deer")
print(zoo) # Output: ['Lion', 'Tiger', 'Giraffe', 'Zebra', 'Deer']

# Delete the animal at the beginning of the list.
zoo.pop(0)
print(zoo) # Output: ['Tiger', 'Giraffe', 'Zebra', 'Deer']

# Print all the animal
for animal in zoo:
    print(animal)
# Print only the first 3 animals
print(zoo[0:3])