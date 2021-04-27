# https://www.codewars.com/kata/5913152be0b295cf99000001
def divisions(n, divisor):
    count = 0
    while n >= divisor:
        n = n // divisor
        count += 1
    return count