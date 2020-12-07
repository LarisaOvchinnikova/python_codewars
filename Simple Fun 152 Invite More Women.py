https://www.codewars.com/kata/58acfe4ae0201e1708000075
def invite_more_women(arr):
        return arr.count(1) > arr.count(-1)

# ---2 case
def invite_more_women(arr):
        return sum(arr) > 0