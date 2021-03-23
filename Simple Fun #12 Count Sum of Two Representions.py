# https://www.codewars.com/kata/5884615cbd573356ab000050
def count_sum_of_two_representations(n, l, r):
    count = 0
    for i in range(l, r+1):
        j = n - i
        if i <= j <= r:
            count += 1
    return count