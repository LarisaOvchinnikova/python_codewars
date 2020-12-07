# https://www.codewars.com/kata/525f039017c7cd0e1a000a26
def palindrome_chain_length(n):
    step = 0
    while str(n) != str(n)[::-1]:
        n = n + int(str(n)[::-1])
        step += 1
    return step