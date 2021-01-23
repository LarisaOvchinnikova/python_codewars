# https://www.codewars.com/kata/5300901726d12b80e8000498
def fizzbuzz(n):
    return ["FizzBuzz" if el % 15== 0 else "Fizz" if el % 3 == 0 else "Buzz" if el % 5 == 0 else el for el in range(1, n+1)]