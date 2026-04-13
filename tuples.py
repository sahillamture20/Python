'''
Tuples
- A tuple is a collection which is ordered and unchangeable.
- Tuples are written with round brackets.
- Tuple items are ordered, unchangeable, and allow duplicate values.
- Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
- Ordered =  it means that the items have a defined order, and that order will not change.
- Unchangeable = meaning that we cannot change, add or remove items after the tuple has been created.
'''
mytuple = ("apple", "banana", "cherry")
print(mytuple)
print(type(mytuple))
print(len(mytuple))
# mytuple[3] = "apple" ==> Will give error - TypeError: 'tuple' object does not support item assignment

# Tuple with duplicate items
thistuple = ("apple", "banana", "apple", "cherry")
print(thistuple)

# Tuple with one item [Note: Add comma after the item]
tuple1 = ("apple",) # comma is important
print(type(tuple1)) # tuple

tuple2 = ("apple") # NOT a tuple, it's string
print(type(tuple2)) # str

# Tuple with different data type
tuple3 = ("abc", 34, True, 40, "male")

# tuple() constructure to make tuple
fruits = tuple(("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"))
print(fruits)

# Access items in the tuple
print(fruits[1]) # banana
print(fruits[-3]) # kiwi

# Range
print(fruits[2:6])
print(fruits[-7:-3])
print(fruits[:5])
print(fruits[6:]) # This will return tuple with last item from tuple "fruits" which will have comma at end like ("mango",) 
print(fruits[:-4])
print(fruits[-3:])

# Check item exists in tuple

if "guava" in fruits:
    print("Yes present")
else:
    print("Not present")

# Steps to Change/Update the tuple
print("Tuple before:", fruits)
# 1) Convert tuple into list using list() constructor
fruits_list = list(fruits)
print(type(fruits_list))

# 2) Change/Update the list
fruits_list.append("jackfruit")
print(fruits_list)

# Convert changed/Updated list back to tuple
fruits = tuple(fruits_list)
print("Tuple after:", fruits) 

# Delete tuple completely usin del keyword
del mytuple
# print(mytuple) ==> This will given error

'''
Packing & Unpacking in TUple:

- When we create a tuple, we normally assign values to it. This is called "packing" a tuple.
- But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking"

Note: The number of variables must match the number of values in the tuple, if not,
      you must use an asterisk to collect the remaining values as a list.
- If the number of variables is less than the number of values, you can add an * to the variable name and
  the values will be assigned to the variable as a list.
- If the asterisk is added to another variable name than the last, Python will assign values to the variable
  until the number of values left matches the number of variables left.

Tuple methods
count()	= Returns the number of times a specified value occurs in a tuple
index()	= Searches the tuple for a specified value and returns the position of where it was found
'''
nuts = ("cashew", "almond", "raisins")
print(nuts)
(green, yellow, red) = nuts

print(green)
print(yellow)
print(red)

# Using Asterisk*
colors = ("green", "red", "yellow", "blue", "pink")

(color1, color2, *remaining_colors) = colors

print(color1)
print(color2)
print(remaining_colors)

# Join 2 tuples
x = ("a", "b" , "c")
y = (1, 2, 3)

z = x + y
print(z)

# Multiply tuple
print(z * 2)

# Loop through tuples