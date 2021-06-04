# Sets are an unordered collection of unique and immutable objects that supports operations corresponding to mathematical set theory.

# By definition, an item appears only once in a set, no matter how many timees it is added. 

x = set('abcde')
y = set('bdxyz')

print(x, y)

print()

print(x - y)  # Difference

print()

print(x | y)  # Union

print()

print(x & y)  # Intersection

print()

print(x ^ y)  # Symmetric difference (XOR)

print() 

print(x > y, x > y)

print('e' in x)

print('e' in 'Camelot', 22 in [11, 22, 33])

print(dir(x))

print()
print()

z =  x.intersection(y)
print(z)

z.add('SPAM')
print(z)

z.update(set(['X', 'Y']))  # Merge: in-[lace union]
print(z)

z.remove('b')

print(z)

print()
print()

# for item in set('abc'): print(item * 3)

for item in 'abc': print(item * 4)

print()
print()

S = set([1, 2, 3])
print(S | set([3, 4]))


print({1, 2, 3, 4})

S1 = {1, 2, 3, 4}
print(S1 - {1, 2, 3, 4})