# https://www.codewars.com/kata/57fe50d000d05166720000b1
def sabb(s, val, happiness):
    count = sum([1 for el in s.lower() if el in "sabbatical"])
    total = count + val + happiness
    return "Sabbatical! Boom!" if total > 22 else "Back to your desk, boy."