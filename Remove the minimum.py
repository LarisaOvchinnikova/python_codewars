#https://www.codewars.com/kata/563cf89eb4747c5fb100001b/python
# def remove_smallest(numbers):
#     if len(numbers) == 0:
#         return []
#     else:
#         m = min(numbers)
#         return [el for i, el in enumerate(numbers) if i != numbers.index(m)]
#

# def remove_smallest(numbers):
#     if len(numbers) == 0:
#         return []
#     m = min(numbers)
#     arr = numbers[:]
#     arr.remove(m)
#     return arr
#
# print(remove_smallest([1,2,3,4,5]))

def remove_smallest(numbers):
    arr = numbers[:]
    if arr:
        arr.remove(min(numbers))
    else:
        return []
    return arr

print(remove_smallest([1,2,3,4,5]))