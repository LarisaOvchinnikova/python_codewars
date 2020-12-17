# https://www.codewars.com/kata/56b97b776ffcea598a0006f2
def bubblesort_once(l):
    a = l[::]
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
    return a