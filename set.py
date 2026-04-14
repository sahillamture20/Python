'''
Set:
- It is a collection which is unordered, unchangeable*, and unindexed.
- Set items are unchangeable, but you can remove items and add new items.
- Sets are written with curly brackets.
- Sets are unordered, so you cannot be sure in which order the items will appear.
- Set items are unordered, unchangeable, and do not allow duplicate values.
- Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

NOTE:
- The values True and 1 are considered the same value in sets, and are treated as duplicates
- The values False and 0 are considered the same value in sets, and are treated as duplicates
'''
# Set example
fruits = {"apple", "mango", "cherry"}
# Output can have above items in anyorder like {'mango', 'cherry', 'apple'} OR {'cherry', 'mango', 'apple'}, etc.
print(fruits) 
print(type(fruits))
print(len(fruits))

# In Set, duplicate values will be ignored
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) # Output: {'apple', 'cherry', 'banana'}

# Set with different data types
set1 = {"abc", 34, True, 40, "male"}

# set() constructor
set1 = set(("red", "blue", "green"))
print(set1)

# Access Items = you cannot access items usin index, but using loops it is possible
for x in set1:
    print(x)

# Check if item exists
print("yellow" in set1) # False
print("red" in set1) # True

# Add items = To add one item to a set use the add() method.
fruits.add("jackfruit")
print(fruits)

# update() method is used to add items to your set from another set, list, tuple, dictionaries, etc.
# The update() changes the original set, and does not return a new set.
tropical = {"pineapple", "mango", "papaya"}
fruits.update(tropical)
print(fruits)

# Remove items = To remove an item in a set, use the remove(), or the discard() method.
# Note: If the item to remove does not exist, remove() will raise an error.
# Note: If the item to remove does not exist, discard() will NOT raise an error.
fruits.remove("pineapple")
print(fruits)
fruits.discard("jackfruit")
print(fruits)

'''
You can also use the pop() method to remove an item, but this method will remove a random item,
so you cannot be sure what item that gets removed.
The return value of the pop() method is the removed item.
'''
fruits.pop()
print(fruits) # cherry got removed

# clear() method empties the set
set1.clear()
print(set1)

# del keyword will delete the set completely
del thisset
# print(thisset) => this will give error saying NameError: name 'thisset' is not defined

# Join the set
# 1) union() method returns all items from all sets. 
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
# set3 = set1.union(set2)
set3 = set1 | set2 | fruits
print(set3)
# It also allows you to join a set with other data types, like lists or tuples. The result will be a set.
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

# NOTE: The | operator only allows you to join sets with sets, and not with other data types. But, the union() method can.
# Both union() and update() will exclude any duplicate items.

# 2) Intersection = It only keeps dulpicates.
# intersection() = It will return a new set, that only contains the items that are present in both sets.
set4 = {"google", "microsoft", "apple"}
# new_set = fruits.intersection(set4)
new_set = fruits & set4
print(new_set) # {"apple"}
# Note: The & operator only allows you to join sets with sets, and not with other data types. But, intersection() method can.

# intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
set4 = {"google", "microsoft", "apple"}
set4.intersection_update(fruits)
print(set4)

# difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
tech = {"google", "microsoft", "apple"}
print("Fruits: ",fruits)
print("Tech: ",tech)
diff_set = fruits.difference(tech)
diff_set1 = fruits - tech
print(diff_set)
print(diff_set1)
# Note: The - operator only allows you to join sets with sets, and not with other data types like you can with the difference() method.

# difference_update() method to keep only the items from the first set that are not present in the other set:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)

# symmetric_difference() method will keep only the elements that are NOT present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

# Both are same
# set3 = set1.symmetric_difference(set2)
set3 = set1 ^ set2

print(set3)
# Note: The ^ operator only allows you to join sets with sets, and not with other data types like you can with the symmetric_difference() method.

# symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)


'''
Frozenset:
- frozenset is an immutable version of a set.
- Like sets, it contains unique, unordered, unchangeable elements.
- Unlike sets, elements cannot be added or removed from a frozenset.


Method	                Shortcut	Description
copy()	 	                        Returns a shallow copy	
difference()	        -	        Returns a new frozenset with the difference	
intersection()	        &	        Returns a new frozenset with the intersection	
isdisjoint()	 	                Returns whether two frozensets have an intersection	
issubset()	            <= / <	    Returns True if this frozenset is a (proper) subset of another	
issuperset()	        >= / >	    Returns True if this frozenset is a (proper) superset of another	
symmetric_difference()	^	        Returns a new frozenset with the symmetric differences	
union()	                |	        Returns a new frozenset containing the union
'''

# Create frozenset using frozenset() constructor
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
