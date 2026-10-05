#  Dictionaries

student = {
    "Name": "Sonika",
    "Age": 19,
    "Branch": "IT"
}

# Kisi ek value ko access karna

print(student)

print(student["Name"])
print(student["Age"])

# New information add karna

student["City"] = "Ajmer"

print(student)

# Existing value change karna

student["Age"] = 20

print(student)

# value check

student = {
    "Name": "Sonika",
    "Age": 19,
    "Branch": "IT"
}

if student["Age"] >= 18:
    print("Adult")
else:
    print("Minor")

# Multiple students

students = {
    "student1": "Sonika",
    "student2": "Ashu",
    "student3": "Annu"
}

print(students["student1"])
print(students["student2"])
print(students["student3"])

# Dictionary mein item delete karna

student = {
    "name": "Sonika",
    "age": 19,
    "branch": "IT"
}

del student["age"]

print(student)