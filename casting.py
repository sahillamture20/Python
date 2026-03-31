"""
Casting is used when you want to specify a type on to a variable.
Casting can be done using constructure functions like below:

1. int() => to convert data types into integers (whole numbers).
            It works great if you give it a string that looks like a number, such as "42".
            However, when you give it "Sahil", the computer gets confused.
2. float()
3. str()

Python uses the Decimal (Base 10) system by default. Since the letters 'S', 'a', 'h', 'i', 'l' do not
exist in the base 10 number system (which only includes digits 0-9), Python throws a ValueError because
it has no mathematical way to translate those characters into a numeric value.
For example: z = int("Sahil")
            ValueError: invalid literal for int() with base 10: 'Sahil'

"""

# int()
x = int(1)
y = int(4.50)
# z = int("Sahil") => It will give valueError
print(x, y)
print(type(x), type(y))

# flaot()
a = float(5)
b = float(6.2)
# c = float("John") => It will given valueError
d = float("5.7")
print(a, b, d)
print(type(a), type(b), type(d))

# str()
m = str(1)
n = str(2.3)
o = str('1j')
print(m, n, o)
print(type(m), type(n), type(o))