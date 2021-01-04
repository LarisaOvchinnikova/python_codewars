# https://www.codewars.com/kata/594ff4005ceb2be738000018
def transform(block):
    l = len(block)
    w = len(block[0])
    block_new = []
    for i in range(w):
        s = []
        for j in range(l):
            s.append(block[j][i])
        block_new.append(s[::-1])
    return block_new