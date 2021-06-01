X = set('spam')
# print(X)
Y = {'h', 'a', 'm'}

print(X, Y)
print(X & Y)
print(X | Y)
print(X - Y)
print({n ** 2 for n in [1, 2, 3, 4]})

print()

print(list(set([1, 2, 1, 3, 1])))

print(set('spam') == set('asmp'))
print('p' in set('spam'), 'p' in 'spam', 'ham' in ['eggs', 'spam', 'ham'])

print(1/3)
print((2/3) + (1/2))

import decimal

d = decimal.Decimal('3.141')
print(d + 1)

decimal.getcontext().prec = 2
print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))

from fractions import Fraction
f = Fraction(2, 3)
print(f + 1)

print(f + Fraction(1, 2))

print( 1 > 2, 1 < 2)
print(bool('spam'))


X = None
print(X)


L = [None] * 100
print(L)

print(type(L))
print(type(type(L)))

if type(L) == type([]):
    print('yes')

if type(L) == list:
    print('yes')

if isinstance(L, list):
    print('yes')


# In Python, we code to object interfaces (the operations supported), not to types. That is, we care what an object does, not waht it is. Not caring about specific types means taht code is automatically applicable to many of them- any object with a compatible interface will work, regardlesss of its specific type.

# Polymorphism is probably the key idea behind using Python well.

