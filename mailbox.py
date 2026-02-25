import math

x_1 = 0.2
x_2 = 0.3
x_3 = 0.45
z = 1938

bottom_box = 2 * (x_1 * x_3) + x_1 * x_2 + 2 * (x_2 * x_3)
top_box = 3.14 * (x_1/2) * (x_1/2) + 3.14 * (x_1/2) * x_2

print(math.ceil((bottom_box + top_box) * z))