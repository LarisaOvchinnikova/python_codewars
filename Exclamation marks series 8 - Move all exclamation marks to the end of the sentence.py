# https://www.codewars.com/kata/57fafd0ed80daac48800019f
def remove(s):
    return s.replace('!', '') + '!' * s.count('!')