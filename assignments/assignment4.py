# Task 1: Working with lists
favorite_fruits = ['apple', 'banana', 'cherry']
print("Original list:", favorite_fruits)
favorite_fruits.append('orange')
print("After adding a fruit:", favorite_fruits)
favorite_fruits.remove('banana')
print("After removing a fruit:", favorite_fruits)
reversed = favorite_fruits[::-1]
print("Reversed list:", reversed)

# Task 2: Exploring dictionaries
dictionary = {
    'name': 'Archita',
    'age': 20,
    'city': 'Atlanta'
}
dictionary['favorite color'] = "Blue"
dictionary['city'] = 'New York'
print("\nKeys:")
for key in dictionary.keys():
    print(key)

print("\nValues:")
for value in dictionary.values():
    print(value)

# Task 3: Working with tuples
my_tuple = ("Inception", "Why Try", "Wonder")
print("\Favorite things:", my_tuple)

try: 
    my_tuple[0] = "New Movie"
except TypeError as e:
    print("Oops! Tuples cannot be changed.")

print("Length of the tuple:", len(my_tuple))
