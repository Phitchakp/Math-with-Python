import math

sin_x = 0.66913

x1 = math.asin(sin_x)       # Radians
x1 = round(math.asin(sin_x), 2)
print(x1)

x2 = math.degrees(math.asin(sin_x))     # Degrees + arcsin
x2 = round(math.degrees(math.asin(sin_x)), 2)     
print(x2)

obtues = 180-x2     # Q2
print(obtues)
print(f"2a. an obtuse angle = {obtues}")


"Go to intro_sin,cos"
"cos_y = -cos121"
# cos_y = -math.cos(120)
cos_y = -math.cos(math.radians(121))
print(cos_y)

# y = math.acos(cos_y)
y = round(math.degrees(math.acos(cos_y)), 2)
print(y)
print(f"2b. an acute angle = {y}")

