# Unicode Text Files

S = 'sp\xc4m'
print(S)
print(S[2])

file = open('unidata.txt', 'w', encoding='utf-8')
file.write(S)
file.close()

text = open('unidata.txt', encoding='utf-8').read()
print(text)
print(len(text))


raw = open('unidata.txt', 'rb').read()
print(raw)
print(len(raw))

text.encode('utf-8')
raw.decode('utf-8')

print(text.encode('latin-1'))
print(text.encode('utf-16'))