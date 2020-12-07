# https://www.codewars.com/kata/556deca17c58da83c00002db
def tribonacci(signature, n):
    if n < 3:
        return signature[:n]
    else:
        for i in range(3, n):
            signature.append(sum(signature[i-3:i]))
    return signature