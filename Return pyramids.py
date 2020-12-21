# https://www.codewars.com/kata/5a1c28f9c9fc0ef2e900013b
def pyramid(n):
    return "".join([" " * (n-i-1) + "/" + " " * i*2 + "\\\n" for i in range(n-1)]) + "/" + "_" * (n * 2 - 2) + "\\\n"