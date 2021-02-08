# https://www.codewars.com/kata/57873ab5e55533a2890000c7
def time_correct(t):
    if t == None: return None
    if t == '': return ''
    if len(t) != 8: return None
    if t.count(":") != 2: return None
    arr = [int(el) for el in t.split(":") if el.isdigit()]
    if len(arr) == 3:
        h, m, s = arr
    else:
        return None
    s1 = s % 60
    m += s // 60
    m1 = m % 60
    h += m // 60
    h = h % 24
    return f"{str(h).rjust(2, '0')}:{str(m1).rjust(2, '0')}:{str(s1).rjust(2, '0')}"
