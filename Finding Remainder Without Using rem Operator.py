https://www.codewars.com/kata/564f458b4d75e24fc9000041
def remainder(dividend,divisor):
    while dividend >= divisor:
        dividend = dividend - divisor
    return dividend