def sum_mix(arr):
    return sum([int(el) for el in arr])

--- 2 case
def sum_mix(arr):
    result = 0
    for i in arr:
        try:
            result += i
        except TypeError:
            result += int(i)
    return result