https://www.codewars.com/kata/5a91a7c5fd8c061367000002/train/python
def minimum_steps(nums, value):
    nums = sorted(nums)
    s = nums[0]
    step = 0
    i = 1
    while s < value:
        s += nums[i]
        step+=1
        i+=1
    return step