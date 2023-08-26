# tuple = collection which is ordered and unchangable used to group together related data
student = ("Bro", 21, "Male")
print(student)
print("\n Count = ", student.count("Bro"))
print("\n Index = ", student.index("Male"))

for stu in student:
    print(stu)

if "Bro" in student:
    print("Bro is here")