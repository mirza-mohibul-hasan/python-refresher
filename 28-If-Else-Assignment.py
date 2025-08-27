"""
If-Else Assignment
- Create a variable grade holding an integer between 0 - 100
- Code if, elif, else statements to print the letter grade of the number grade variable

Grades:
A = 90 - 100
B = 80 - 89
C = 70-79
D = 60 - 69
F = 0 - 59
Example:
if grade = 87 then print('B')
"""
grade = 87
if grade >= 90 and grade <= 100:
    print("A")
elif 80 <= grade <= 89: # If two variable are same then we can write "80 <= grade <= 89"
    print("B")
elif 70 <= grade <= 79:
    print("C")
elif 60 <= grade <= 69:
    print("D")
else:
    print("F")