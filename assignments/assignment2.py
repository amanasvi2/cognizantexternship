# Task 1: Counting Down with a While Loop
# This asks the user for a starting number
num = int(input("Enter a starting number: "))
# This wil countdown from the starting number to 1
while num > 0:
    print(num)
    num -= 1
print("Blast off!")

# Task 2: Multiply Table with a For Loop
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Task 3: Find the Factorial of a Number
num = int(input("Enter a number: "))
for i in range(1, num + 1):
    if i == 1:
        factorial = 1
    else:
        factorial *= i
print(f"The factorial of {num} is {factorial}")