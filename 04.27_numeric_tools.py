import math
print(math.pi, math.e)
print(math.sin(2 * math.pi / 180))
print(math.sqrt(144), math.sqrt(2))

print(min(3, 1.4, 2.2, 4))
print(math.floor(2.567))
print(math.floor(-2.56))
print(math.trunc(2.567))
print(math.trunc(-2.567))


# Floor (next lower integer)
# Truncate (drop decimal digits)
# Round

print(round(2.567, 2))

print('%.1f' % 2.567, '{0:.2f}'.format(2.567))

print(math.sqrt(144))
print(144 ** .5)
print(pow(144, .5))

import random
print(random.random())
print(random.randint(1, 10))
print(random.randint(1, 10))

print(random.choice(['Life of Brian', 'Holy Grail', 'Meaning of Life']))

suits = ['hearts', 'clubs', 'diamonds', 'spades']
random.shuffle(suits)
print(suits)