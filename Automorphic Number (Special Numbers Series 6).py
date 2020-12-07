#https://www.codewars.com/kata/5a58d889880385c2f40000aa/train/python
def automorphic(n):
    return "Automorphic" if str(n**2).endswith(str(n)) else "Not!!"