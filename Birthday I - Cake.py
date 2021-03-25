# https://www.codewars.com/kata/5805ed25c2799821cb000005
import string
def cake(candles,s):
    if candles == 0: return 'That was close!'
    alph = string.ascii_lowercase
    return 'That was close!' if sum([ord(s[i]) if i % 2 == 0 else alph.index(s[i])+1 for i in range(len(s))]) <= (0.7 * candles) else 'Fire!'