https://www.codewars.com/kata/54ff0d1f355cfd20e60001fc
def factorial(n):
    res = 1
    for i in range(1,n+1):
        res = res * i
    if 0 <= n <= 12:
        return res
    else:
        raise ValueError