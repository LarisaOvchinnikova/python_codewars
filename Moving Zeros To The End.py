# https://www.codewars.com/kata/52597aa56021e91c93000cb0
def move_zeros(array):
    non_zeros = []
    count = 0
    for el in array:
        if type(el) in [int, float] and el == 0:
            count+=1
        else:
            non_zeros.append(el)
    return non_zeros + [0] * count