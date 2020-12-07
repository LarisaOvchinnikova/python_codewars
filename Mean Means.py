#https://www.codewars.com/kata/57c6b44f58da9ea6c20003da
def geo_mean(nums, arith_mean):
    miss = arith_mean * (len(nums) + 1) - sum(nums)
    p = miss
    for el in nums:
        p *= el
    geom_mean = p ** (1/(len(nums)+1))
    return geom_mean