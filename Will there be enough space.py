# https://www.codewars.com/kata/5875b200d520904a04000003
def enough(cap, on, wait):
    return 0 if cap - on >= wait else wait - (cap - on)