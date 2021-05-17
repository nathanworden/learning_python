# Strings are immutable in Python - they cannot be changed in place after they are created. You can never overwrite the values of immtable objects.

S = 'Spam'

# S[0] = 'z'


# numbers, strings, and tuples are immutable

#  lists, dictionaries, and sets are not

S = 'shrubbery'
L = list(S)
print(L)

print(L[1])

L[1] = 'c'

print(L)

print(''.join(L))


print()

B = bytearray(b'spam')
B.extend(b'eggs')
print(B)

S = 'Spam'
print(S.find(''))