# Lists have no fied size

# Python doesn't allow us to reference items that are not present.

# Indexing off the end of a list is always a mistake, but so is assigning off the end:

L = [123, 'spam', 1.23]

print(L)
# print(L[99])   # IndexError: list inde out of range

L[2] = 1
print(L)

L.append(5)

print(L)