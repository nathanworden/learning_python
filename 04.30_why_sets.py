L = [1, 2, 1, 3, 2, 4, 5]
print(set(L))

L = list(set(L))
print(L)


print(set('spam') - set(['h', 'a', 'm']))


print(set(dir(bytes)) - set(dir(bytearray)))