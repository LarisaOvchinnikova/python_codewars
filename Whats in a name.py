# https://www.codewars.com/kata/59daf400beec9780a9000045
def name_in_str(st, name):
    st = st.lower()
    for el in name.lower():
        if el in st:
            i = st.index(el)
            st = st[i+1:]
        else:
            return False
    return True