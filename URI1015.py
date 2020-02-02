import math


x1, y1 = raw_input().split(" ")

x1 = float(x1)
y1 = float(y1)

x2, y2 = raw_input().split(" ")

x2 = float(x2)
y2 = float(y2)

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("{:.4f}".format(distance))

'''
2.5 -0.4
-12.2 7.0

16.4575
'''