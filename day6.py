# Creating a list 

fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits)

# Changing a existing item

fruits = ["Apple", "Banana", "Mango", "Orange"]

fruits[1] = "Grapes"

# Adding a new item at the end of the list

print(fruits)

fruits = ["Apple", "Grapes", "Mango", "Orange"]

fruits.append("Pineapple")

# Accessing list items using index

print(fruits)

print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[4])

# Adding an item at a specific position

fruits.insert(1, "Watermelon")
print(fruits)

# Removing an item from the list

fruits.remove("Watermelon")

print(fruits)

# Removing an item using its index

fruits.pop(2)

print(fruits)

# Finding the number of items in the list

print(len(fruits))

# Checking if an item exists in the list

print("Apple" in fruits)
print("Banana" in fruits)

# Day 6 - Practice

students = ["Sonika", "Ashu", "Annu"]

# Add a new student at the end

print(students)
students.append("Monu")
print(students)

# Change Ashu to Monu

students[1] = "Monu"
print(students)

# Add Neha at index 1

students.insert(1, "Neha")

print(students)

# Remove Annu

students.remove("Annu")
print(students)

# Print total number of students

print(len(students))

# Check if Sonika is in the list

print("Sonika" in students)