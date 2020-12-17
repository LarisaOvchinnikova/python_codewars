# https://www.codewars.com/kata/596925532f709fccf3000077
def fizzbuzz_plusplus(nums, words):
    n = 1
    for el in nums:
        n *= el
    arr = list(range(1, n+1))
    lst = []
    for elem in arr:
        s = ''
        for i, el in enumerate(nums):
            if elem % el == 0:
                s += words[i]
        if s == '':
            lst.append(elem)

        else:
            lst.append(s)
    return lst