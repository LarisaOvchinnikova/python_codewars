# https://www.codewars.com/kata/5b0148133e9715bf6f000154
def hi_all():
    one = len([[]])
    two = one + one
    three = two + one
    four = two * two
    five = four + one
    six = two * three
    seven = six + one
    eight = two * four
    nine = three * three
    ten = two * five
    H = chr(six * six + six * six)
    e = chr(ten * ten + one)
    l = chr(ten * ten + eight)
    o = chr(ten * ten + ten + one)
    space = chr(ten * three + two)
    w = chr(ten * eight + seven)
    r = chr(ten*ten + seven*two)
    d = chr(ten * ten)
    word = H+e+l+l+o+space+w+o+r+l+d
    return word