# Distance Between Two Points

import math


x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

z1 = (x2 - x1)**2
z2 = (y2 - y1)**2

distance = math.sqrt(z1 + z2)

print('{:.4f}'.format(distance))
