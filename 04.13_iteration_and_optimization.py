# An object is iterable if it is either a physicallys stored  sequence in memor, or
# it is an object that generates one item at a time in the context of an iteration operation.

squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
print(squares)

squares = []
for x in [1, 2, 3, 4, 5]:
    squares.append(x ** 2)

print(squares)