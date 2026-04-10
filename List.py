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

# Change the item value in list using index of that item
fruits[1] = "mango"
print(fruits)
fruits[1:2] = ["pineapple", "orange"] # Here I'm trying to change 1 item, but giving 2 items, then list will get adjusted
print(fruits)
print(len(fruits)) # 4 
fruits[1:3] = ["mango"] # Here I'm trying to change 2 items, t=but giving 1 item, then list will get adjusted
print(fruits)
print(len(fruits)) # 3

# insert() methods is used to insert item at specified index
fruits.insert(3, "kiwi")
print(fruits)
print(len(fruits)) # 4

# append() method is used to add item in the end of the list
fruits.append("watermelon")
print(fruits)
print(len(fruits)) # 5

# extend() method is used to append items from one list to another
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
nuts = ["cashew", "peanut", "almond"]
fruits.extend(nuts)
print(fruits)
print(len(fruits))

# remove() method removes mentioned item 
fruits.remove("almond")
print(fruits)
print(len(fruits))
print(fruits.pop(6) + " got removed, because fruits only.")
print(fruits)
print(len(fruits))
print(fruits.pop()) # It will remove last item from the list
print(fruits)
print(len(fruits))

# 'del' keyword will also remove the item from the list using index
del fruits[0]
print(fruits)
print(len(fruits))
print(name)
del name
# print(name) = this will throw error

# clear() method empties the list
print(list1)
list1.clear()
print(list1)

'''
sort() = sort the list alphanumerically, ascending, by default
       = it will change the original list
       = To sort descending, use the keyword argument reverse = True
       = While sorting case sensitive items, items startin with capital letters & all capital letters get first priority
         over small letters. 
'''
print("List of fruits before soritng = ", fruits)
fruits.sort()
print("List of fruits after sorting = ", fruits)
fruits.sort(reverse = True)
print("List of fruits after sorting in descending order = ", fruits)
fruits.append("Guava")
print(fruits) # Output: ['watermelon', 'mango', 'kiwi', 'cherry', 'Guava']
fruits.sort()
print(fruits) # Output: ['Guava', 'cherry', 'kiwi', 'mango', 'watermelon']
fruits.append("Banana")
print(fruits)
fruits.sort(key = str.lower) # Output: ['Banana', 'cherry', 'Guava', 'kiwi', 'mango', 'watermelon']
print(fruits)

# reverse() method reverses the current sorting order of the elements.
fruits.reverse()
print(fruits) # Output: ['watermelon', 'mango', 'kiwi', 'Guava', 'cherry', 'Banana']

'''
Copy List = You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1,
            and changes made in list1 will automatically also be made in list2.

There are 3 ways to copy list
1. copy() = built-in method for copying
2. list() = built-in method for copying
3. slicing = Use slice syntax without start and end like [:] 
'''
# copy()
healty_fruits = fruits.copy()
print(healty_fruits)

# list()
available_fruits = list(fruits)
print(available_fruits)

# slicing method
fav_fruits = fruits[:]
print(fav_fruits)

# Join list using + operator
list2 = mylist + fruits
print(list2)

#Join using extend() method
mylist.extend(fruits)
print(mylist)

''''
We will see below topic when we learn loops:
1 Another way to loop through item of one list and use append() method to add them in another list
2 Loop list
3 list comprehension
'''''