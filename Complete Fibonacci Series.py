# https://www.codewars.com/kata/5239f06d20eeab9deb00049b
def fibonacci(n):
    arr = [0,1]
    for i in range(2, n):
        arr.append(arr[i-1] + arr[i-2])
    return arr[0:n] if n > 0 else []