# https://www.codewars.com/kata/5a043724ffe75fbab000009f
def reverse_middle(lst):
    m = len(lst) // 2
    return lst[m-1:m+2][::-1] if len(lst) % 2 != 0 else lst[m-1:m+1][::-1]