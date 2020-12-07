https://www.codewars.com/kata/5a4138acf28b82aa43000117/train/python
def adjacent_element_product(arr):
    return max([arr[i] * arr[i+1] for i in range(len(arr)-1)])