# https://www.codewars.com/kata/59decdf40863c76ae3000080
def max_consec_zeros(n):
    n = bin(int(n))[2:]
    s = ''
    for el in n:
        if el=="1": s+=' '
        else: s+="0"
    s = s.split()
    if s == []: return "Zero"
    s = max([len(el) for el in s])
    digits =['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen']
    return digits[s]