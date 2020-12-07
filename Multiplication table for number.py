#https://www.codewars.com/kata/5a2fd38b55519ed98f0000ce/train/python
def multi_table(n):
    return "\n".join([f"{i} * {n} = {i*n}" for i in range(1, 11)])