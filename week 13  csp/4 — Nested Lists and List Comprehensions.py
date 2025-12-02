list1 = [1, 2, 3]
print(list1[-1]) 
list2 = [4, 5, 6]
print(list2[0]) 
nested_list = [list1, list2]
print(nested_list[0]) # output: [1, 2, 3]
print(nested_list[1]) # output: [4, 5, 6]
print(nested_list[0][1]) # output: 2
print(nested_list[1][0]) # output: 4

fruits = ["apple", "banana", "cherry"]
vegetables = ["carrot", "lettuce", "spinach"]
meats = ["chicken", "beef", "turkey"]
grocery_list = [fruits, vegetables, meats]
print(grocery_list[2][-1]) # output: turkey
print(grocery_list[1][0])  # output: carrot
print(grocery_list[0][1])  # output: banana 
for collection in grocery_list:
    for food in collection:
        print(food, end=" ")
    print()#


#create a keypad normally found on phones in parentheses
num_pad = (
    ("1", "2", "3"),
    ("4", "5", "6"),
    ("7", "8", "9"),
    ("*", "0", "#") )
for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()

# for i in range(1,10001):
#     for j in range(1,10001):
#         if i>0 and j>0:
#             for k in range(1,10001):
#                 print("the number is:", i, j, k)

# Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])    # 6

# List comprehension
first_col = [row[0] for row in matrix]
print(first_col)       # [1, 4, 7]



# Practice Problems:

# Build a matrix variable containing 3 lists of 3 numbers each.
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
# Print the first list.
print(matrix[0])
# Print the second item from the third list.
print(matrix[2][1])
# Use a list comprehension to extract the last item from each sub-list.
sub_list = [row[-1] for row in matrix]
print(sub_list)# output: [30, 60, 90]
# Challenge: Create a new list containing squares of numbers from 1–10 using a comprehension.
squares = [x**2 for x in range(1, 11)]
print(squares)  # output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]