# Decimals are like floating point numbers but they have a fixed number of decimal points. Hence, decimals are fixed-precision floating-point values.

print(0.1 + 0.1 + 0.1 -0.3)

from decimal import Decimal
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))