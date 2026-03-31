a,b,c=10,15,20
print(a+b+c)


a=b=c=25
print(a+b+c)


# Output variable
m = "Learning pythn is easy"
print(m)


x = 5
y = "Sahil"
"""
print(x+y) // TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""
print(x,y)

# Global Variable
x = "GLOBAL"

def myfunc():
    print("Variable x is",x,"variable")

myfunc()

# global keyword
def myfunc():
    global y
    y = "global"

myfunc()

print("We make our variable y global variable using keyword '"+ y+"'.")
print("Use the global keyword if you want to change a global variable inside a function.")