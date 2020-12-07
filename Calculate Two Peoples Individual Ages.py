# https://www.codewars.com/kata/58e0bd6a79716b7fcf0013b1
def get_ages(sum_, difference):
    if difference < 0 or sum_ < 0 or sum_ < difference:
        return None
    a = (sum_ - difference) / 2
    b = (sum_ + difference) / 2
    return (a, b) if a > b else (b, a)