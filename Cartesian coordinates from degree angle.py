#https://www.codewars.com/kata/555f43d8140a6df1dd00012b/train/python
import math
def coordinates(degrees, radius):
    return round(radius * math.cos(math.pi * degrees/180),10), round(radius * math.sin(math.pi * degrees/180), 10)