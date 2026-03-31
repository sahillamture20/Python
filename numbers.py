"""
There are three numeric types in Python:
1. int: Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
2. float: Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
          Float can also be scientific numbers with an "e" to indicate the power of 10.
3. complex: Complex numbers are written with a "j" as the imaginary part.
Variables of numeric types are created when you assign a value to them.
"""

x=1
y=3.14
z=1j

print(type(x))
print(type(y))
print(type(z))

# Type Conversion
a=float(x)
b=int(y)
c=complex(x)

print(a)
print(b)
print(c)

"""
Random Number: Python does not have a random() function to make a random number,
               but Python has a built-in module called random that can be used to make random numbers.
"""

# Import the random module, and display a random number from 1 to 9.

import random

print("The random number between 1 to 10 is",random.randrange(1, 10))
    