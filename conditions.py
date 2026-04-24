'''
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b

How 'if' keyword works?
- if keyword check if given expression is true or false
- if answer is true then 1st code block runs, otherwise 2nd code block runs
- Indentation = Python relies on indentation (whitespace at the beginning of a line) to define scope in the code.
- Boolean variables can be used directly in if statements without comparison operators.

Python can evaluate many types of values as True or False in an if statement.
- Zero (0), empty strings (""), None, and empty collections are treated as False. Everything else is treated as True.
- This includes positive numbers (5), negative numbers (-3), and any non-empty string
- Even "False" is treated as True because it's a non-empty string.

elif keyword:
- Similar to saying "if the previous conditions were not true, then try this condition".
- You can have as many elif statements as you need. Python will check each condition in order and execute
  the first one that is true.
- Only the first true condition will be executed. Even if multiple conditions are true,
  Python stops after executing the first matching block.

else keyword:
- catches anything which isn't caught by the preceding conditions.
- else statement is executed when if condition is evaluated to false.
- The else statement must come last. You cannot have an elif after an else.
- Its useful for error handling, validation, and providing default values as acting fallback.

Python Logical Operators: Python has three logical operators:

1) and - Returns True if both statements are true
2) or - Returns True if one of the statements is true
3) not - Reverses the result, returns False if the result is true

You can combine multiple logical operators in a single expression.
Python evaluates not first, then and, then or.

and Operator Truth Table:
Condition 1	Condition 2	Result
   True        	True	True
   True        	False	False
   False       	True	False
   False       	False	False

or Operator Truth Table:
Condition 1	Condition 2	Result
   True        	True	True
   True        	False	True
   False       	True	True
   False       	False	False

Pass statement: 

-> if statements cannot be empty, but if you for some reason have an if statement with no content,
   put in the pass statement to avoid getting an error. 
-> The pass statement is a null operation - nothing happens when it executes. It serves as a placeholder.

Why Use pass?
- The pass statement is useful in several situations:
- When you're creating code structure but haven't implemented the logic yet
- When a statement is required syntactically but no action is needed
- As a placeholder for future code during development
- In empty functions or classes that you plan to implement later
'''
# if keyword
a, b = 10, 24
if a < b:
    print(f"{b} is greater than {a}")
else:
    print(f"{b} is smaller than {a}")

# elif keyword 
c, d = '33' # Iterable Unpacking
if c > d:
    print(f"{c} is biger than {d}.")
elif c == d:
    print(f"{c} and {d} are equal.")

# Shorthand if
x = 5
y = 2
if x > y: print("x is greater than y")

# Ternary operator / Conditional expression
a = 2
b = 330
print("A") if a > b else print("B") 

# pass statement
age = 16

if age < 18:
  pass # TODO: Add underage logic later
else:
  print("Access granted")