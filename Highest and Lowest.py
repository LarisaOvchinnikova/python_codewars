# https://www.codewars.com/kata/554b4ac871d6813a03000035
def high_and_low(numbers):
    arr = numbers.split(" ")
    arr = [int(el) for el in arr]
    arr = sorted(arr)
    return str(arr[-1]) + " " + str(arr[0])