https://www.codewars.com/kata/5868812b15f0057e05000001

def tail_swap(strings):
    s1 = strings[0].split(':')
    s2 = strings[1].split(':')
    return [s1[0] + ':' + s2[1], s2[0] + ':' + s1[1]]