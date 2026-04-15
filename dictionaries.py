'''
Dictionary:
- Dictionaries are used to store data values in key:value pairs.
- A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
- Dictionaries are written with curly brackets.
- Dictionary items are ordered, changeable, and do not allow duplicates.
- Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
- Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

Note:
- As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(type(thisdict))
print(len(thisdict))
print(thisdict["brand"])
print(thisdict["year"]) # Output: 1964
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2000
}
print(thisdict["year"]) # Output: 2000, because duplicate values will overwrite existing values

# dict() constructor is used to create dictionary
dict1 = dict(name = "John", age = 36, country = "Norway")
print(dict1)

# Access items in dictionary
# 1)  Using the key
print(dict1["name"])
# get() method
print(dict1.get("age"))
# keys() method will return list of all the keys in the dictionary
print(dict1.keys())
# values() method will return a list of all the values in the dictionary.
print(dict1.values())
# items() method will return each item in a dictionary, as tuples in a list.
print(dict1.items())
# Check if key exists
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

'''
Change dictionary items in below 2 ways:
1. Using key name
2. Using update() method
'''
# Using key name
dict1["country"] = "New York"
print(dict1)
# Using update() method
dict1.update({"name": "Tony"})
print(dict1)

'''
Adding new item to dictionary is done by 2 ways:
1. Using new kwy and value
2. Using update() method
'''
# 1. Using new key-value pair
dict1["Job"] = "SRE"
print(dict1)
# 2. Using update() method
dict1.update({"surname" : "Stark"})
print(dict1)

'''
There are 4 ways to remove item/items from dictionary
1. pop() method will remove the item with the specified key name
2. popitem() method removes the last inserted item
3. del keyword removes the item with the specified key name. It can also delete dictionary completely.
4. clear() method empties the dictionary
'''
# 1. pop() mehtod
thisdict.pop("year")
print(thisdict)
# 2. popitem()
thisdict.popitem()
print(thisdict)
# 3. clear()
thisdict.clear()
print(thisdict)
# 4. del keyword
del thisdict
# print(thisdict) ==> This will given error saying "NameError: name 'thisdict' is not defined"

'''
Copy dictionary:
You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1,
and changes made in dict1 will automatically also be made in dict2.

One way is to use the built-in Dictionary method copy().
We can also use dict() onstructor to copy dictionary.
'''
mydict = dict1.copy()
print(mydict)
copied_dict = dict(dict1)
print(copied_dict)

'''
Nested Dictionary: A dictionary can contain dictionaries, this is called nested dictionaries.

'''
# Example of nested dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

# If you want to add three dictionaries into a new dictionary, then create three dictionaries, then create one dictionary
# that will contain the other three dictionaries
grp1 = {
  "name" : "Steve",
  "year" : 2004
}
grp2 = {
  "name" : "Thor",
  "year" : 2007
}
grp3 = {
  "name" : "Natasha",
  "year" : 2011
}
mygroup = {
  "grp1" : grp1,
  "grp2" : grp2,
  "grp3" : grp3
}
print(mygroup)

# Access Items in Nested Dictionaries
# To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary.
print(myfamily["child2"]["name"])