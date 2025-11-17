# # Objective:
# # Students will understand how to create, modify, and access elements in Python lists.

# # Topics Covered:
# # Creating lists, indexing, slicing, appending, popping, sorting, reversing.

# # Examples:

# my_list = ['apple', 'banana', 'cherry']
# print(my_list[0])         # apple
# print(my_list[1:])        # ['banana', 'cherry']

# my_list.append('grape')
# print(my_list)

# my_list.pop(1)
# print(my_list)

# numbers = [3, 1, 4, 2]
# numbers.sort()
# print(numbers)


# # Practice Problems:

# Create a list with 5 of your favorite foods
foods = ["pizza", "sopes", "tacos", "pasta", "ice cream"]

# Print the second and last item
print(foods[1])   # second item
print(foods[-1])  # last item

# Add a new item using .append()
foods.append("ramen")
print(foods)

# Remove the first item using .pop(0)
foods.pop(0)
print(foods)

# Reverse your list using .reverse()
foods.reverse()
print(foods)


# colections are used to store multiple items in a single variable
# lists are ordered collections of items
# lists are mutable meaning you can change their content
# lists are created using square brackets []
list_of_fruits = ["apple", "banana", "cherry", "date"]
print(list_of_fruits)
print(type(list_of_fruits))
print(list_of_fruits[0])
print(list_of_fruits[1])
print(list_of_fruits[-1])
print(list_of_fruits[1:3])
#reversing a list
list_of_fruits.reverse
print(list_of_fruits)
print(list_of_fruits[::-1])
list_of_fruits.append("elderberry")
list_of_fruits.append("Mango")
list_of_fruits.append("Strawberry")
list_of_fruits.extend(["Lemon", "Blueberry", "Tomato"])
print(list_of_fruits[::-1])
popped_item = list_of_fruits.pop()
print(popped_item)
print(list_of_fruits)
list_of_fruits.insert(1, "Honeydew")
print(list_of_fruits)
list_of_fruits.remove("banana")
print(list_of_fruits)
list_of_fruits.insert(3, "Lime")
print(list_of_fruits)
list_of_items = list(range(1,101))
print(list_of_items)
list_of_items = list(range(1,1001))
print(list_of_items)
print(len(list_of_items))
list_of_items.extend(range(1001, 2001))
print(list_of_items)
#why use a list 
# instead or creating separate variables for each item we can store them in a list this makes our job easier this makes managing the complexity of our code easier when we need to manage multiple items performance task answer 

# sets and tuples
# sets and tuples are a;so park of the collections family of python
set1 = {1, 2, 3, 4, 5}
set2 = {"apple", "banana", "cherry"}
print(set1)
print(set2)
set_with_duplicates = {1, 2, 2, 3, 4, 5}
print(set_with_duplicates)
print(3 in set1)
print(6 in set1)
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ("apple", "banana", "cherry")
print(tuple1)
print(tuple2)
# tuples are immutable meanning they cannot be chagned after creation, for storing data that should not be modified 