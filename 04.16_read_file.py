f = open('dataaaa.txt')
text = f.read()
print(text)

print(text.split())

print()

for line in open('dataaaa.txt'): print(line)

print()

print(dir(f))
print(help(f.closed))