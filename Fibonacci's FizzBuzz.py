# https://www.codewars.com/kata/57bf599f102a39bb1e000ae5
def fibs_fizz_buzz(n):
    f = [1, 1]
    for i in range(2, n):
        f.append(f[i-1] + f[i-2])
    for i in range(len(f)):
        if f[i] % 15 == 0:
            f[i] = "FizzBuzz"
        elif f[i] % 3 == 0:
            f[i] = "Fizz"
        elif f[i] % 5 == 0:
            f[i] = "Buzz"
    return f[:n]