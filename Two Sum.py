# https://www.codewars.com/kata/52c31f8e6605bcc646000082/train/python
def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return i, j

# --- 2 case:
def two_sum(numbers, target):
    dct = {}
    for i, num in enumerate(numbers):
        if target - num in dct:
            return dct[target - num], i
        dct[num] = i