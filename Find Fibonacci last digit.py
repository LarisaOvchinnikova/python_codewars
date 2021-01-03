# https://www.codewars.com/kata/56b7251b81290caf76000978
def get_last_digit(index):
    f1 = 1
    f2 = 1
    i = 3
    while i <= index:
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        i += 1
    return f3 % 10