https://www.codewars.com/kata/5a3e1319b6486ac96f000049/
def pairs(arr):
    return len([(arr[i],arr[i+1]) for i in range(0,len(arr)-1, 2) if abs(arr[i]-arr[i+1]) == 1])