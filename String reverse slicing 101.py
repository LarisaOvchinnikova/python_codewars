# https://www.codewars.com/kata/586efc2dcf7be0f217000619
def reverse_slice(s):
    s = s[::-1]
    return [s[i:] for i in range(len(s))]