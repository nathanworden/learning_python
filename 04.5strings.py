S = 'Spam'
print(S[1:3])

# X[I:J], means "give me everything in  from offset I up to but not including offset J"

print(S[1:])
print(S)
print(S[0:3])
print(S[0:4])
print(S[:-1])
print(S[:])    # All of S as a top-level copy (0:len(S))

print(S + 'xyz')
print(S)
print()
print(S * 8)