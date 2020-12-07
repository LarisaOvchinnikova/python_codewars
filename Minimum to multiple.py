https://www.codewars.com/kata/5e030f77cec18900322c535d
def minimum(a, x):
    div_before = a // x
    rem = a % x
    div_aft = div_before + 1
    rem_plus = x * div_aft - a
    return min(rem, rem_plus)

#2 case
def minimum(a, x):
    return min(x - a % x, a % x)