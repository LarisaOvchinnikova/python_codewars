# https://www.codewars.com/kata/55caf1fd8063ddfa8e000018
def arithmetic_sequence_elements(a, r, n):
    arr = []
    for i in range(n):
        arr.append(a)
        a += r
    return ", ".join([str(el) for el in arr])

#2 case
def arithmetic_sequence_elements(a, r, n):
    return ", ".join([str(a+r*i) for i in range(n)])