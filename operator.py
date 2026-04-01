name = "sahil"
a = 3

# Arithmatic operators
print(1+1) # 2
print(2-1) # 1
print(2*2) # 4
print(5/2) # 2.5
print(5%2) # It gives remainder
print(4**2) # Exponentiation: Its 4 power 2, ives square of 4, 4 x 4 = 16 
print(5//2) # Floor division: performs division but round-off the result to nearest whole integer, 5/2=2.5 round off to 2

# Assignment operator used to create varible or we can say that used to assign value to variable at the time of initialization.
a += 2 # a = a + 2 = 3 + 2 = 5
print(a)
a -= 2 # a = a - 2 = 5 - 2 = 3
print(a)
a *= 2 # a = a * 2 = 3 * 2 = 6
print(a)
a %= 2 # a = a % 2 = 8 % 2 = 0
print(a)

# Comparison Operator
a = 13
b = 33

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

# Bitwise Operator => act on bits and perform bit-by-bit operations. These are used to operate on binary numbers.
a = 10
b = 4

print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)

# Logical operator
condition1 = True
condition2 = False

print(not condition1) # False
print(condition1 and condition2) # False
print(condition1 or condition2) # True

# Identity Operator
'''
"is" and "is not" are the identity operators & both are used to check if two values are located on the same part of
the memory. Two variables that are equal do not imply that they are identical. 

is      => True if the operands are identical 
is not  => True if the operands are not identical
'''
a = 10
b = 20
c = a

print(a is not b)
print(a is c)

# Membership Operator
'''
Membership Operators => "in" and "not in" are the membership operators that are used to test whether a value or
                        variable is in a sequence.

in      => True if value is found in the sequence
not in  => True if value is not found in the sequence
'''
print('S' in name) # True
print('s' in name) # False
print('l' not in name) # False
print('j' not in name) # True

# Ternary Operator
'''
Ternary Operator => It evaluate something based on a condition being true or false.
                    It also known as conditional expressions. 
                    It was added to Python in version 2.5. 

It simply allows testing a condition in a single line replacing the multiline if-else, making the code compact.

Syntax :  [on_true] if [expression] else [on_false] 
'''
a, b = 10, 20
min = a if a < b else b

print(min)

'''
Difference between == and is operator in Python =>

== Operator (Equality Operator) =>
It is used when you want to check whether two objects contain same data (value),
regardless of whether they are stored in same memory location.
Internally, it calls __eq__() method of class.
For built-in types like lists, strings and numbers, this means checking if the contents are same.

is Operator (Identity Operator) =>
The is operator is used when you want to check whether two variables refer to exact same object in memory.
It does not care about values.
Even if two objects look identical, it will return False unless both variables literally point to the same memory location.

'''