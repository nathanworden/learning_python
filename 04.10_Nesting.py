# Python's core data types support arbitrary nesting

M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

# print(M)
# print(M[1])
print(M[1][2])

#  List comprehension expression

col2 = [row[1] for row in M]
print(col2)
print()
print(M)

# List comprehensions derive from set notation; they are a way to build a new list by running an expression on each item in asequence, one at a time.

print()
col2_plus_one = [row[1] + 1 for row in M]
print(col2_plus_one)

print()
col2_conditional = [row[1] for row in M if row[1] % 2 == 0]
print(col2_conditional)

print()
diag = [M[i][i] for i in [0, 1, 2]]
print(diag)


print()
doubles = [c * 2 for c in 'spam']
print(doubles)

print(list(range(10)))
print()
print(list(range(-6, 7, 2)))

print()

print([[x ** 2, x ** 3] for x in range(4)])