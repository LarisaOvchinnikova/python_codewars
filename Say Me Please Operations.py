https://www.codewars.com/kata/5b5e0c0d83d64866bc00001d
def say_me_operations(nums):
    nums = [int(el) for el in nums.split()]
    arr = []
    for i in range(2, len(nums)):
        if nums[i] == nums[i-2] + nums[i-1]:
            arr.append("addition")
        elif nums[i] == nums[i-2] - nums[i-1]:
            arr.append("subtraction")
        elif nums[i] == nums[i-2] * nums[i-1]:
            arr.append("multiplication")
        elif nums[i] == nums[i-2] // nums[i-1]:
            arr.append("division")
    return ", ".join(arr)