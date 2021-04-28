https://www.codewars.com/kata/592e2446dc403b132d0000be
def maximum_product(arr):
    r = []
    p = 1
    for i in range(len(arr)):
        p = 1
        for j in range(len(arr)):
            if i != j:
                p *= arr[j]
        r.append(p)
    return min([arr[i] for i, el in enumerate(r) if el == max(r)])