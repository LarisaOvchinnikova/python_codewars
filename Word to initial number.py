# https://www.codewars.com/kata/5bb148b840196d1be50000b1
def convert(st):
    st = st.lower()
    if st == '': return 0
    dct = {st[0]: 1}
    j = 0
    for i in range(1, len(st)):
        if st[i] not in dct:
            dct[st[i]] = j
            if j == 0:
                j+=2
            else:
                j+=1
    return int("".join([str(dct[el]) for el in st]))