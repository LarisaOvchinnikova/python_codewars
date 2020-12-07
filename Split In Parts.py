https://www.codewars.com/kata/5650ab06d11d675371000003
def split_in_parts(s, part_length):
    res = ''
    for i in range(0, len(s), part_length):
        res = res + s[i: i+ part_length] + " "
    return res[:-1]

def split_in_parts(s, part_length):
    return " ".join([s[i: i+ part_length] for i in range(0, len(s), part_length)])