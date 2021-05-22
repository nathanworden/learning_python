# Japanese and Russian alphabet characters are outside the ASCII set. Such non-ASCII text can show up in web pages, emails GUIs, JSON, XML, or elsewhere. When it does, handling it well requires Unicode support.

#  Python has such support built in, but the form of its Unicode support varies per Python line, and is one of their most prominent differences.

#  In Python 3.X, the normal `str` string handles Unicode text.

print('sp\xc4m')    # normal str strings are Unicode text
print(b'a\x01c')    # byte strings are bypte-based data
print(u'sp\u00c4m') # The 2.X Unicode literal works in 3.3+: just str

print()

print(u'sp\xc4m')
print('a\x01c')