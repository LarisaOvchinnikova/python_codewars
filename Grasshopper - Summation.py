# Grasshopper - Summation
# https://www.codewars.com/kata/55d24f55d7dd296eb9000030
def summation(num):
    sum = 0
    i = 1
    while i <= num:
        sum = sum + i
        i = i + 1
    return sum

# --- 2 case

def summation(num):
    return sum(list(range(1,num+1)))


def summation(num):
    return sum(range(1, num+1))