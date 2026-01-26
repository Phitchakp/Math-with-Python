import math

" *** Python, all angles expect to be {radians}, not be {degrees}"
" degrees = radians * (180/pi)"


a1 = math.cos(60)
print(a1)
" Calculate(degrees) = 60 * (180/3.14) = 3,437.74 "
"                    = 3,437.74/360 = 9.5 rotation circle)"
" ** cos of 60 radians"


a2 = math.cos(math.radians(60))
print(a2)
" Calculate(radians) = 60 * (pi/180) = pi/3"
" cos(pi/3) = 1/2, 0.5"
" ** cos of pi/3 radians"


a3 = math.cos(math.degrees(60))
print(a3)
" ** cos of 3,437.75 radians"


" *** all angles must be converted to {radians} first if you are start with {degrees}"
