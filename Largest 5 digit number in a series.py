https://www.codewars.com/kata/51675d17e0c1bed195000001
def solution(digits):
    n = str(digits)
    arr = [int(n[i:i+5]) for i in range(len(n)-4)]
    return max(arr)