# https://www.codewars.com/kata/577c349edf78c178a1000108
def xmastree(n):
    w = n * 2 - 1
    tree = []
    for i in range(1, n+1):
        tree.append(("#"*(i*2-1)).center(w, "_"))
    tree.extend(["#".center(w, "_")] * 2)
    return tree