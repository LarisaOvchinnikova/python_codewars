https://www.codewars.com/kata/598d89971928a085c000001a
def sort_number(a):
    a = sorted(a)
    a[-1] = 1 if a[-1] != 1 else a[-1] + 1
    return sorted(a)