M = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

G = (sum(row) for row in M)
print(next(G))
print(next(G))
print(next(G))

print(list(map(sum, M)))

print('sets and dictionaries')

print({sum(row) for row in M})
print()
print(list(map(sum, M)))
print(map(sum, M))

print()

print({sum(row) for row in M})

print([ord(x) for x in 'spaam'])