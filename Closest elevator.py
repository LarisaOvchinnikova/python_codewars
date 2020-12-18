# https://www.codewars.com/kata/5c374b346a5d0f77af500a5a
def elevator(left, right, call):
    return 'left' if abs(call - left) < abs(call - right) else 'right'