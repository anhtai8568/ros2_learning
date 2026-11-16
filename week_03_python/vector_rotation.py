import math

x = 1
y = 0
rad = math.radians(90)
x_new = x * math.cos(rad) - y * math.sin(rad)
y_new = x * math.sin(rad) + y * math.cos(rad)
print(x_new, y_new)   
