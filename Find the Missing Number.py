# https://www.codewars.com/kata/57f5e7bd60d0a0cfd900032d
def missing_no(nums):
    s = sum(range(1, max(nums)+1)) - sum(nums)
    return s if s > 0 else 0 if 0 not in nums else max(nums)+ 1

# 2case
def missing_no(nums):
    return 5050 - sum(nums)