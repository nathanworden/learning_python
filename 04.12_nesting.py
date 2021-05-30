rec = {'name': {'first': 'Bob', 'last': 'Smith'},
        'jobs': ['dev', 'mgr'],
        'age': 40.5}
print(rec)

print(rec['name'])
print(rec['name']['last'])
print(rec['jobs'])
print(rec['jobs'][-1])
rec['jobs'].append('janitor')
print(rec)

rec = 0

print(rec)

# garbage collection is a automatic process that cleans up unused memory as your program runs and frees you from having to manage such details in your code.

print()

D = {'a': 1, 'b': 2, 'c': 3}
print(D)
D['e'] = 99
print(D)

# print(D['f']) # error

print('f' in D)

if not 'f' in D:
    print('missing')

if not 'f' in D:
    print('missing')
    print('no, really...')

value = D.get('x', 0)

print(value)


value = D['x'] if 'x' in D else 0
print(value)

Ks = list(D.keys())
print(Ks)
Ks.sort()
print(Ks)

for key in Ks:
    print(key, '=>', D[key])


print(D)

for key in sorted(D):
    print(key, '=>', D[key])


print('test')
x = 4
while x > 0:
    print('spam!' * x)
    x -= 1

