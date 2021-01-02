# https://www.codewars.com/kata/515ceaebcc1dde8870000001
def solution(items, index, default_value):
    return items[index] if 0 <= abs(index) <= len(items) else default_value