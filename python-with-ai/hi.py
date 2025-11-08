# import requests

# # Download a web page
# response = requests.get("https://api.github.com")
# print(response.status_code)  # Should print 200

# name = "daisy"
# age = 19
# isstudent = True
# len(name)
# nowname = name * 5;
# canvote = age>=18

#is19 = age == 19 here is19 cnat be selected alone 


# age = 25
# has_license = True
# # AND - both must be true
# can_drive = age >= 16 and has_license
# print(can_drive)  # True

# is_adult = age >= 18
# is_child = not is_adult
# print(is_child)  # False

# name = "daisy"
# print(f"My name is {name}")

# text = "python Programming"

# print(text.lower())      # "python programming"
# print(text.upper())      # "PYTHON PROGRAMMING"
# print(text.title())      # "Python Programming"

# messy = "  hello world  "
# print(messy.strip())     # "hello world" (removes whitespace)

# price = "$19.99"
# print(price.strip("$"))  # "19.99"


# message = "I love Python programming with Python"


# # Check if something exists
# print("Python" in message)        # True
# print(message.startswith("I"))   # True
# print(message.endswith("Python")) # True

# # Find position
# print(message.find("Python"))     # 7 (first occurrence)
# print(message.count("Python"))    # 2 (number of times)

# # Replace
# new_message = message.replace("Python", "JavaScript")
# print(new_message)  # "I love JavaScript programming with JavaScript"

# score = 85

# if score >= 90:
#     print("A - Excellent!")
# elif score >= 80:
#     print("B - Good job!")
# elif score >= 70:
#     print("C - Keep it up!")
# else:
#     print("F - Need improvement")

#LOOPS:
 for i in range(5):
  print(i) #not 5

#     # Count from 1 to 5
# for i in range(1, 6):
#     print(i)
# # Output: 1, 2, 3, 4, 5

# # Count by 2s
# for i in range(0, 10, 2):
#     print(i)
# Output: 0, 2, 4, 6, 8

# name = "Python"
# for i in name:
#     print(i)

# colors = ["red", "blue", "green"]
# for i in colors:
#     print(f"I like {i}")

# Output:
# I like red
# I like blue
# I like green

# count = 0
# while count < 5:
#     print(f"Count is {count}")
#     count = count + 1 

# fruits = ["apple", "banana", "orange"]

# # Change an item
# fruits[0] = "mango"
# print(fruits)  # ["mango", "banana", "orange"]

# # Add items
# fruits.append("grape")      # Add to end
# fruits.insert(1, "kiwi")    # Insert at position

# # Remove items
# fruits.remove("banana")     # Remove by value
# last = fruits.pop()        # Remove and return last
# del fruits[0]              # Remove by index

#IMPORTANT!!!!!!!!!!!!!!
numbers = [1, 2, 2, 4]
numbers = [i for i in numbers if i!= 2]
print(numbers)

#=----------------------------------------
#dict
person = {
    "name" : "daisy",
    "age": 19,
    "course" : "cse"
}
print(person["name"])       # "Alice"
print(person["age"])        # 30
scores = dict(math=95, english=87, science=92)
scores = {"math": 95, "english": 87, "science": 92}
#they don't have spaces or start with a number). 
print(person.get("job"))    # None (no error)
print(person.get("job", "Unknown"))

person["email"] = "day@email.com"  # Add new
person["age"] = 20
print(person)

# del person["email"]              # Remove by key
# age = person.pop("age")          # Remove and return
# person.clear()
# print(person)

print(person.keys())    # dict_keys(['name', 'age', 'city'])
print(person.values())  # dict_values(['Alice', 30, 'New York'])
print(person.items())   

# Check if key exists
if "name" in person:
    print("Name found!")

# Update multiple values
person.update({"age": 18, "job": "Engineer"})


# Dictionary of dictionaries
students = {
    "alice": {"age": 20, "grade": "A"},
    "bob": {"age": 21, "grade": "B"},
    "charlie": {"age": 19, "grade": "A"}
}

# Access nested data
print(students["alice"]["grade"])  # "A"


#------------------------------------------
# Empty tuple
empty = ()

# Tuple with items
point = (3, 5)
colors = ("red", "green", "blue")
coordinates = 10, 20
# Single item tuple needs comma!
single = (42,)  # Note the comma

colors = ("red", "green", "blue")
print(colors[-1])    # "blue"
# Slicing works too
print(colors[0:2]) 

point = (3, 5)
x, y = point  # x = 3, y = 5

# Multiple assignment
a, b, c = 1, 2, 3  # Same as (1, 2, 3)

# Swap variables elegantly
x, y = y, x  # Swaps values!
single = (42,)
print(type(single))  # <class 'tuple'>

# Wrong - tuples are immutable
point = (3, 5)

# Right - create a new tuple
point = (4, point[1])
print(point)
# Or convert to list, modify, convert back
temp = list(point)
temp[0] = 4
point = tuple(temp)
print(point)

#-----------------------------------------------
# Empty set (careful!)
empty_set = set()  # NOT {} - that's a dict!

# Set with values - both ways work
numbers = {1, 2, 3, 4, 5}
fruits = set(["apple", "banana", "orange"])

# From a list (removes duplicates)
scores = [85, 90, 85, 92, 90]
unique_scores = set(scores)  # {85, 90, 92}

colors = {"red", "blue"}

# Add items
colors.add("green")
print(colors)  # {'red', 'blue', 'green'}

# Remove items
#colors.remove("blue")    # Error if not found
colors.discard("blue") # No error if not found
print(colors)
# Check membership
if "red" in colors:
    print("Red is available")

names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
unique_names = list(set(names))
print(unique_names)  # ['Alice', 'Bob', 'Charlie']

allowed_users = {"alice", "bob", "charlie"}
if "alice" in allowed_users:  # Very fast!
    print("Access granted")

#-------------------------------------------
#FUNC
# Bad - using global variable
total = 0

def add_to_total(amount):
    global total
    total += amount

# Good - using parameters and return
def add_amounts(current_total, amount):
    return current_total + amount

total = 0
total = add_amounts(total, 10)
total = add_amounts(total, 20)
print(total)  # 30

# RIGHT - Required first, optional last
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Now it works:
greet("Alice")           # Output: Hello, Alice!
greet("Bob", "Hi")       # Output: Hi, Bob!

# Wrong - don't use lists as defaults
def add_item(item, list=[]):
    list.append(item)
    return list

# Right - use None and create new list
def add_item(item, list=None):
    if list is None:
        list = []
    list.append(item)
    return list

def find_max_min(val):
    return min(val), max(val)

nums = [5,3,10,8]

minimum, maximum = find_max_min([5,3,10,8])
print(f"Min: {minimum}, Max: {maximum}")
#or
mini,maxi = find_max_min(nums)
print(f"Min: {mini}, Max: {maxi}")
#or
result = find_max_min([5,3,10,8])
print(result)

#-----------------------PACKAGES-------------------
import datetime
today = datetime.date.today()
print(today)

import os
current_dir = os.getcwd()
print(current_dir)

# JSON data
import json
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)
