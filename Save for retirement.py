https://www.codewars.com/kata/58177df1e7f457b89d000327/train/python

def calculate_retirement(yearly_deposit, min_target_balance):
    dct = {}
    for rate in range(1, 7):
        s = 0
        year = 0
        while s <= min_target_balance:
            s += yearly_deposit
            s += s*rate/100
            year += 1
        dct[rate] = year
    return dct