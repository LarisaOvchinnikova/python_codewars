# https://www.codewars.com/kata/59706036f6e5d1e22d000016
def words_to_marks(s):
    st = " abcdefghijklmnopqrstuvwxyz"
    return sum([st.index(i) for i in s])