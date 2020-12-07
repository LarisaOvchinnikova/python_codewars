# https://www.codewars.com/kata/5eb27d81077a7400171c6820/train/python
import math
def graceful_tipping(bill):
    bill = math.ceil(bill * 1.15)
    n = 10
    q = 1
    while True:
        if bill < n:
            while bill % q != 0:
                bill += 1
            return bill
        n *= 10
        q = n // 20
    return bill
