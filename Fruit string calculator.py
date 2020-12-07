# https://www.codewars.com/kata/57b9fc5b8f5813384a000aa3/train/python
def calculate(s):
    nums = [int(el) for el in s.split() if el.isdigit()]
    op = s.find("loses")
    return nums[0] - nums[1] if op != -1 else nums[0] + nums[1]