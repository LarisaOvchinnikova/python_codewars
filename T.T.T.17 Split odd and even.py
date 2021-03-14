# https://www.codewars.com/kata/57a2ab1abb994466910003af
def split_odd_and_even(n):
    n = str(n)
    r = n[0]
    for i in range(1, len(n)):
        if (int(n[i-1]) + int(n[i])) % 2 != 0:
            r += " " + n[i]
        else:
            r += n[i]
    return [int(el) for el in r.split(' ') ]