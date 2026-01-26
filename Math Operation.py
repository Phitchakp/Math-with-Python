a=5

sum =a
sum +=3

minus =a
minus -=3

multi =a
multi *=3

divided =a
divided /=3

divided_round = round(divided, 2)

remainder =a
remainder %=3

expo =a
expo **=3


print(f"Sum = {sum}")
print(f"Minus = {minus}")
print(f"Multi = {multi}")
print(f"Divided = {divided}")
print(f"Divided_round = {divided_round}")
print(f"Remainder = {remainder}")
print(f"Expo = {expo}\n")


"-------------------------------------------------"
b = -4
c = 9

abso = abs(b)
power = pow(a,3)
max_number = max(a,b,c)
min_number = min(a,b,c)

print(f"Absolute = {abso}")
print(f"Power = {power}")
print(f"Max = {max_number}")
print(f"Min = {min_number}\n")


"-------------------------------------------------"
import math
d =8.1

pi = math.pi
e = math.e
root = math.sqrt(c)
round_up = math.ceil(d)
round_down = math.floor(d)

print(f"Pi = {pi}")
print(f"e = {e}")
print(f"Root = {root}")
print(f"Round_Up = {round_up}")
print(f"Round_Down = {round_down}\n")


"-------------------------------------------------"
# radius = float(input("Radius of Circle= "))
radius = 7
circumference = 2 * math.pi * radius
area = math.pi * pow(radius, 2)

print(f"Radius = {radius}")
print(f"Circumfernce = {round(circumference, 2)}")
print(f"Area = {round(area, 2)}\n")


a1 = 7
b1 = 24
c1 = math.sqrt(pow(a1,2) + pow(b1,2))

print(f"Side C = {c1}")