age = int(input("Enter your age: "))

if age >= 18:
    print("You are an Adult")
else:
    print("You are a Minor")

    marks = int(input("Enter your marks: "))

    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 60:
        print("Grade C")
    else:
        print("Grade D")
number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
