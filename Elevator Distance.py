# https://www.codewars.com/kata/59f061773e532d0c87000d16

def elevator_distance(arr):
    return sum([abs(arr[i+1]-arr[i]) for i in range(len(arr)-1)])