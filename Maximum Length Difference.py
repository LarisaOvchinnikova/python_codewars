# https://www.codewars.com/kata/5663f5305102699bad000056/train/python
def mxdiflg(a1, a2):
    if len(a1) == 0 or len(a2) == 0:
        return -1
    l1 = [len(el) for el in a1]
    l2 = [len(el) for el in a2]
    ma1 = max(l1)
    mi1 = min(l1)
    ma2 = max(l2)
    mi2 = min(l2)
    return max(abs(ma1-mi2), abs(ma2-mi1))