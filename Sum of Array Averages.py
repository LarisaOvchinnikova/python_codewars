https://www.codewars.com/kata/56d5166ec87df55dbe000063/train/python
import math
def sum_average(arr):
    return math.floor(sum([sum(el)/len(el) for el in arr]))