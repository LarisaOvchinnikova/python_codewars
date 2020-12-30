# https://www.codewars.com/kata/5d532b1893309000125cc43d
def number_of_hooks(length,max_hook_dist):
    if length <= max_hook_dist: return 2
    n = 2
    while length / n > max_hook_dist:
        n *= 2
    return n + 1