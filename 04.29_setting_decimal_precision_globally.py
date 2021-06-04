import decimal
print(decimal.Decimal(1) / decimal.Decimal(7))

# The default is 28 digits for decimals

decimal.getcontext().prec = 4
print(decimal.Decimal(1) / decimal.Decimal(7))

print(1999 + 1.33)

decimal.getcontext().prec = 1
pay = decimal.Decimal(str(1999 + 1.33))
print('hello')
print(pay)


from fractions import Fraction
x = Fraction(1, 3)
y = Fraction(4, 6)

print(x, y)
print(x + y)
print(x - y)
print(x * y)

print(Fraction('.25'))


a = 1 / 3.0
b = 4 / 6.0

print(a)
print(b)

print(Fraction(1, 10) + Fraction(1, 10) + Fraction(1, 10) - Fraction(3, 10))

print((1/3) + (6 / 12))

print(Fraction(6, 12))
print(Fraction(1, 3) + Fraction(6, 12))

print((2.5).as_integer_ratio())

f = 2.5
z = Fraction(*f.as_integer_ratio())
print(z)
print(x)
print(x + z)
print(float(x))

print(x)
print(x + 2)
print(x + 2.0)
print(x + (4./3))
print(x + Fraction(4, 3))