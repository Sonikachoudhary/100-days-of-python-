print("Numbers from 1 to 5:")
for i in range(1, 6):
    print(i)

print("\nEven numbers:")
for i in range(2, 11, 2):
    print(i)

print("\nOdd numbers:")
for i in range(1, 10, 2):
    print(i)

print("\nWhile loop: ")
i = 1

while i <= 5:
    print(i)
    i = i + 1

print("\nCountdown: ")
i = 5

while i >= 1:
    print(i)
    i = i - 1

print("Blast off!")

print("\nPrint sum of the number 1 to 5: ")
i = 1
sum = 0

while i <= 5: 
    sum = sum + i
    i = i + 1

print("Sum = ", sum )
