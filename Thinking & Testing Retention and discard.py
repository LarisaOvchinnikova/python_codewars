# https://www.codewars.com/kata/56ee0448588cbb60740013b9
def mystery(n):
    return [i for i in range(1, n+1, 2) if n % i == 0]