# https://www.codewars.com/kata/57eaec5608fed543d6000021/train/python
def div_con(arr):
    return sum([el if type(el) == int else -int(el) for el in arr])