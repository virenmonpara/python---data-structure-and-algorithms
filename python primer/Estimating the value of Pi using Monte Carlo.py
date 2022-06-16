import math
import random

scatter_object_circle = 0
scatter_object_square = 0

interval = 1000
for i in range(interval):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if math.sqrt(x**2 + y**2) <= 1:
        scatter_object_circle += 1
    scatter_object_square += 1

pi = 4*scatter_object_circle/scatter_object_square

print('estimated and original value of pi is :', pi, ',', math.pi)
