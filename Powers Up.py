# https://www.codewars.com/kata/6001f1b46aad3700080d20a7
def powers_up(number, up_to):
    s = 0
    n = number
    for i in range (1, up_to+1):
        s += n
        n = n * number
    return s