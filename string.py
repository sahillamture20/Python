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


# upper(), lower(), title()
print("sahil".upper()) # SAHIL
print("SAHIL".lower()) # sahil
print("sAHIL lAMTURE".title()) # Sahil Lamture

'''
Slicing = Used to return range of characters from string using indexes and slice syntax
Slice syntax = Inside square brackets mention start and end index separated by colon.
The indexing start from 0.
'''
b = "I am learning Python"
# print(len(b), b[19])

# Slice from index 3 to index 9, charater at 9th index will not include
print("The sliced charaters from string "+b+" is '"+b[3:9]+"'")

print(b[:7]) # Here start index is not mentioned, so python consider it from 1st charater i.e. index 0

print(b[5:]) # Here end index is not mentioned, so python consider last till last character i.e. len(b) - 1

# Negetive index is used to slice string from back. Negetive index start from -1.
print(b[-8:-4])

# The upper() method returns the string in upper case:
print(b.upper())

# The lower() method returns the string in lower case:
print(b.lower())

# The strip() method removes any whitespace from the beginning or the end:
print(" I am Sahil ".strip())

# The replace() method replaces a string with another string:
print(" I am Sahil ".replace("S", "R"))

# The split() method returns a list where the text between the specified separator becomes the list items.
print(b.split("n"))

'''
f-string = We can concatenate 2 strings using '+', but we can't concatenate string with other data type variable using
'+'. For that requirement we can using f-string or format() method.

print(a+2) => THis will throw error saying "TypeError: can only concatenate str (not "int") to str"

Placeolder & Modifier =
- Placeholder means whatever written inside the {} brackets in f-string.
- A placeholder can contain variables, operations, functions, and modifiers to format the value.
- A placeholder can include a modifier to format the value.
- A modifier is included by adding a colon : followed by a legal formatting type.
'''

# f-string
age = 25
print(f"{a} is {age} year's old.") # Sahil is 25 year's old.

price = 59
# .2f is a modifier which is written with price variable as part of placeholder
txt = f"The price is {price:.2f} dollars"
print(txt)

'''
format() = In older code, you'll see empty curly braces {} used as positional placeholders.
Python fills them in order based on the arguments passed to .format().
The {} are placeholders waiting for data
'''
text = "The {} is running on port {}.".format("server", 8080)
print(text)

'''
Escape charaters = 
- An escape character is a backslash \ followed by the character you want to insert.
- To insert characters that are illegal in a string, use an escape character.
- An example of an illegal character is a double quote inside a string that is surrounded by double quotes.
Example: 
txt = "We are the so-called "Vikings" from the north."
'''
txt = "We are the so-called \"Vikings\" from the north."
print(txt)