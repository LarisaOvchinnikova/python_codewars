# https://www.codewars.com/kata/565ce4ab24ef4aee6a000074
def is_matching(st, st1, st2):
    st = st.replace(' ', '').lower()
    st1 = st1.replace(' ', '').lower()
    st2 = st2.replace(' ', '').lower()
    return sorted(st) == sorted(st1 + st2)
