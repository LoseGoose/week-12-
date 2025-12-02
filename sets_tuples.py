# sets and tuples examples:
# set examples:
set1 = {1, 2, 3, 4, 5} 
print(set1) 
print(type(set1)) 
set1.add(6)
print(set1)
set1.remove(2)
print(set1)

#sets drop duplicates
set2 = {"apple", "banana", "apple", "cherry"}
print(set2)

# tuple examples:
tuple1 = (10, 20, 30, 40, 50)
print(tuple1)
print(type(tuple1))
#tuples are immutable, meaning you cannot change their content
# this ,aeks tuples useful for storing data that should not be modified
social_security_number = (12333333, 4555555, 67676767)
print(social_security_number) 