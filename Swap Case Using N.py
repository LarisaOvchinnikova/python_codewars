# https://www.codewars.com/kata/5f3afc40b24f090028233490
def swap(s,n):
    b = (bin(n)[2:] * len(s))[0:len(s)]
    res = ''
    i = 0
    for el in s:
        if el.isalpha():
            if b[i] == "1":
                res += el.swapcase()
            else:
                res += el
            i+=1
        else:
            res+=el
    return res