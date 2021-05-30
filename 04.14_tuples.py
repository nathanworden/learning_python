T = (1, 2, 3, 4)
print(T)
print(len(T))
T += (5, 6)
print(T)
print(T[0])


# Tuples are like a list that cannot be changed. Tuples are sequences, like lists, but they are immutable, like strings. Functionally, they're used to represent fixed collections of items: the components of a specific calendar date, for instance. Syntactically, they are normally coded in parentheses instead of square brackets, and they support arbitrary types, arbitrary nesting, and the ussual sequence operations.

# Typles also have type specific callable metods, but not nearly as many as lists

print(T.index(4))
print(T.count(4))

# T[0] = 2 # Typles canot be changed once created. They are immutable sequences.

T = (2,) + T[1:]
print(T)

T = 'spam', 3.0, [11, 22, 33]
print(T)