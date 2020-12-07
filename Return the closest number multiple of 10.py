https://www.codewars.com/kata/58249d08b81f70a2fc0001a4
def closest_multiple_10(i):
    return round(i / 10) * 10

def closest_multiple_10(i):
    last_digit = i % 10
    if last_digit < 5:
        return i // 10 * 10
    else:
        return (i // 10 + 1) * 10
