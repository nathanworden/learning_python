# File objects are Python code's main interface to external files on your computer. They can be used to read and write text memos, audio clips, Excel documents, saved email messages, and whatever else you happen to have stored on your machine. Files are a core type byt they're something of an oddball- therei s no specific literal syntax or creating them. Rather, to create a file object, you cal the built-in open function, passing an external filename and an optional processing mode as strings.

f = open('dataaaa.txt', 'w')
f.write('Hello\n')
f.write('world\n')
f.write('call me maybe ')
f.write('its so crazy')
f.close()

# This creates a file in the current directory and writes text to it (the filenae can be a full direcory path if you need to access a file elsewhere on your computer).