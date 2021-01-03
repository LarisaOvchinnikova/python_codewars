# https://www.codewars.com/kata/589ebcb9926baae92e000001
def convert(s):
    return "".join([chr(int(s[i:i+2])) for i in range(0, len(s)-1, 2)])