# https://www.codewars.com/kata/59c3e819d751df54e9000098
def get_consective_items(items, key):
    items = str(items)
    key = str(key)
    longest = 0
    arr = []
    for el in items:
        if el == key:
            longest += 1
        else:
            arr.append(longest)
            longest = 0
    arr.append(longest)
    return max(arr)