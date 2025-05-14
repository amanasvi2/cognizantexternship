# Task 1: String Slicing and Indexing
string = "Python is amazing!"
# 1. Print the first 6 characters of the string.
print("First word: " + string[:6])  # Output: Python
# 2. Print the word amazing.
print("Amazing part: " + string[10:17])  # Output: amazing
# 3. Print the entire string in reverse.
print("Reversed string: " + string[::-1])  # Output: !gnimaza si nohtyP

# Task 2: String Methods
string = " hello, python world! "
print("Modified string: " + string.strip().capitalize().replace("world", "universe").upper())  # Output: HELLO, PYTHON UNIVERSE!

# Task 3: Check for Palindrome
string = input("Enter a string to check if it's a palindrome: ")
def is_palindrome(string):
    # Remove spaces and convert to lowercase
    cleaned_string = string.replace(" ", "").lower()
    if cleaned_string == cleaned_string[::-1]:
        print(f"Yes, {string} is a palindrome.")
    else:
        print(f"No, {string} is not a palindrome.")

is_palindrome(string)