"""
Notes:
1. In Python, strings are array of characters. There is no data type called character in Python.
2. We can used square brackets to access specific charater using its position. In array, positioning starts from 0.
"""

# String example
a = "Sahil"
print(a)

# Multiline string example
b = """My name is Sahil
I am a DevOps Engineer.
Next job title/position I am looking is MLOps Engineer or AI Engineer.
This is how you write multiline string in Python.
You can use 3 single quotes also instead of double.
"""
print(b)

# Print 3rd position character from varible 'a'
print(a[2])


# Looping through string is possible as strings are considered as array 
for x in a:
    print(x)


# String length is calculated using built-in 'len()' funtion
print(len(a))

# Python has keyword 'in' which is used to check if any specific text/pharse/character is present in the string.
# Similarly there is another keyword in Python called 'not in' which check if  any specific text/pharse/character is NOT present in the string.
# Both keywords returns true or false as output.
print('S' in a) # True
print('s' in a) # False
print('l' not in a) # False
print('j' not in a) # True

'''
isinstance() function is used to check if variable is instance of specified class.
In below example, 'str' is class & we are using python's built-in function 'isinstance()' to check if
variable 'a' is instance of class 'str' or not.
'''
print(isinstance(a, str)) # True
