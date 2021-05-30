# Python dictionaries are mappings

# Mappings are collections of other objects, but they store objects by key instead of by relative position.

# Dictionaries are mutable: like lists, they may be changed in place and can grow and shrink on demand.

D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}

print(D)

print(D['food'])

D['quantity'] += 1

print(D)

D = {}
D['name'] = 'Bob'
print(D)

bob1 = dict(name='Bob', job='dev', age=40)
print(bob1)

bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40]))
print(bob2)

