https://www.codewars.com/kata/56f3a1e899b386da78000732
def partlist(arr):
    return [(" ".join(arr[0:i]), " ".join(arr[i:])) for i in range(1,len(arr))]