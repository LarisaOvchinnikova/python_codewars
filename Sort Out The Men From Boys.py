# https://www.codewars.com/kata/5af15a37de4c7f223e00012d
def men_from_boys(arr):
    arr = list(set(arr))
    men = sorted([el for el in arr if el % 2 == 0])
    boys = sorted([el for el in arr if el % 2 != 0], reverse=True)
    return men +  boys