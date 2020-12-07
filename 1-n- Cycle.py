# https://www.codewars.com/kata/5a057ec846d843c81a0000ad
def cycle(n) :
    if n%2==0 or n%5==0:
        return -1
    d = 9
    count = 1
    while d % n != 0:
        d = d%n*10 + 9
        count += 1
    return count

a = pwo