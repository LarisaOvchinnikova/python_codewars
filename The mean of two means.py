# https://www.codewars.com/kata/583df40bf30065fa9900010c
def get_mean(arr,x,y):
    return (sum(arr[:x]) / x + sum(arr[-y:])/y) / 2 if 1 < x <= len(arr) and 1 < y <= len(arr) else -1