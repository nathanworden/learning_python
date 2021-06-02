# Expression Operators

# Expressions are a combination of numbers (or other objects) and operators that compute a value when executed by Python


# print(5 ^ 6)
# print(5 << 1)

M = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

col2 = [row[1] for  row in M]

print(col2)

tuple = (5, 6)
print(tuple)

print(40 + 3.14)

print(int(3.1415))

a = 3
b = 4
print(a + 1, a - 1)
print(b * 3, b / 2)
print(a % 2, b ** 2) # 1, 16
print(2 + 4, 2.0 ** b)  # 6, 16
print(b / 2 + a) # 5.0
print(b / (2.0 + a))
print(b / (2.0 + a))