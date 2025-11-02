a = 10
b = a
print(b)
print(a is b)
b = 20
print(a is b)
a = 10+17
print (type (a))
a = 4+4.0
print (type (a))
a = 4/4
print (type (a))
a = 4/4
print (a)
a = 15 % 4
print (a)
print(2 ** 8)
import math
a = math.sqrt(64)
print(a)
import math
r = 10
print(2 * math.pi * r)
print(type(2 * math.pi * r))
print(15 ** 42)
print(120 // 12 == 120 / 12)
print (20 // 5)

print(True == 1)

a = 10
if a >= 10:
    b = 1
else:
     b = 0
print(b)
my_variable = 11
print(my_variable % 2 == 0)
print(5 + (10 > 5) * 3)
print(5 + (10 < 5) * 3)
print(3 * 4 - 8 * 2 * (7 - 5.0) + 2)
print((10 + 2) / 3 * (15.0 == 15) - 4)
print((15.0 == 15))
print(hex(0xb64))
print(0xb64 == 2916)
print(type(hex(0xb64)))
print(0xb64 + 0o77)
print(oct(99))
print(-0x4d2)
print(oct(-30 ** 99999))
print(hex(-30 ** 99999))
from decimal import Decimal
print(99.1 < Decimal("99.1"))
a = "string"
b = 'string'
c = """string"""
d = '''string'''
print(a == b == c == d)
a = "проприетарный"[3]