# https://www.codewars.com/kata/5a084a098ba9146690000969
def time_convert(num):
    if num <= 0: return "00:00"
    h = str(num // 60).rjust(2, "0")
    m = str(num % 60).rjust(2, "0")
    return f"{h}:{m}"