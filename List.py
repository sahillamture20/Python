'''
List is a one of 4 built-in data structure in Python used to store an ordered collection of items.
They are dynamic, resizable and capable of storing multiple data types.
The other 3 built-in data structure in Python are Tuple, Set, and Dictionary.

- Allows duplicate elements
- Mutable: list elements can be changed, updated, added, or removed after the list is created.
- Ordered: elements maintain the order in which they are inserted.
- Index-based: elements are accessed using their position, starting from index 0.
- Heterogeneous: a list can store different data types such as integers, strings, booleans and even other lists.
'''

# Create list = [] brackets are used to create list
mylist = [24, 5, 77, 43, 90] # Int data type list
print(mylist)
fruits = ["apple", "banana", "cherry"] # String data type list
print(fruits)
list1 = ["abc", 34, True, 40, "male"] # List with mixed data types
print(list1)

# Length of the list
print("Length of list 'mylist' is",len(mylist))
print("Lenth of list 'fruits' is", len(fruits))
print("Length of list 'list1' is", len(list1))

# Type of a list
print(type(mylist))
print(type(fruits))
print(type(list1))

# List creation using list() constructor = Pass tuple, string or another list to list() constructor
name = list(("sahil"))
print(name)

# Access list item using index
print(mylist[0]) # 1st item
print(fruits[2]) # item at index 2 i.e. 3rd item from fruit list
print(name[-3]) # It will print 3rd item 'h' from the back, as we are using negetive index. Negetive index starts from -1.
print(mylist[2:4]) # Slicing / Range of index, Output given small list: [77, 43]
print(name[:2])
print(list1[3:])
print(name[-3:-2])
print(fruits[-2:])
print(fruits[:-2])

# Check if item exists
if "mango" in fruits:
    print("Yes")    # Yes
else:
    print("It's time to buy some mango...")