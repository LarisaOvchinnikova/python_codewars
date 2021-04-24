# https://www.codewars.com/kata/5c3433a4d828182e420f4197
def reverse(a):
    l = [len(el) for el in a];
    st = "".join(a)[::-1]
    arr = []
    i = 0
    while len(st)> 0:
        arr.append(st[:l[i]])
        st = st[l[i]:]
        i += 1
    return arr