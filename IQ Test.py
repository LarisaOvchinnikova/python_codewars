# https://www.codewars.com/kata/552c028c030765286c00007d
def iq_test(numbers):
    lst = numbers.split()
    count_even = 0
    count_odd = 0
    for el in lst:
        if int(el) % 2 == 0:
            count_even += 1
            x = el
        else:
            count_odd += 1
            y = el
    if count_even == 1:
        return lst.index(x) + 1
    else:
        return lst.index(y) + 1