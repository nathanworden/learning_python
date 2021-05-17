S = 'Spam'
print(S.find('pa'))
print(S)
print(S.replace('pa', 'XYZ'))
print(S)


print()
line = 'aaa,bbb,cccc,dd'
splitted_line = line.split(',')
print(splitted_line)

print()

print(S)
print(S.lower())
print(S.upper())
print(S.isalpha())
print(S.isdigit())

line = 'aaa,bbb,ccccc,dd    '
print(line.rstrip())