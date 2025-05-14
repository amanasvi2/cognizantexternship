# Project 3: Password Strength Checker
# Description: This program checks the strength of a password based on various criteria.
password = input("Enter a password: ")
import re
score = 0

# Checking 
# Check for length
if len(password) >= 8:
    score += 2
else:
    print("Password is too short. It must be at least 8 characters long.")

# Check for at least one uppercase letter
if any(char.isupper() for char in password):
    score += 2
else:
    print("Password needs at least one uppercase letter.")

# Check for at least one lowercase letter
if any(char.islower() for char in password):
    score += 2
else:
    print("Password needs at least one lowercase letter.")

# Check for at least one digit
if any(char.isdigit() for char in password):
    score += 2
else:
    print("Password needs at least one digit.")

# Check for at least one special character
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 2
else:
    print("Password needs at least one special character (e.g., @, #, $).")

# Display the password strength score
print(f"Your password strength score is: {score}/10")

# Final message based on the score
if score == 10:
    print("Your password is very strong! 💪")
elif score >= 6:
    print("Your password is moderately strong.")
else:
    print("Your password is weak. Consider improving it.")