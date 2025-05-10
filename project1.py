#This is asking the user for their age and checking if they are eligible to vote
age = int(input("How old are you? "))
years = 18 - age

# This is the conditional statement that checks if the user is eligible to vote
if age >= 18:
    print("Congratulations! You're eligible to vote.")
else:
    print(f"Sorry, you're not eligible to vote yet. But only {years} left to go!")
