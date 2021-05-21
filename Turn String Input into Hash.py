# https://www.codewars.com/kata/52180ce6f626d55cf8000071
def str_to_hash(st):
    if st == '': return {}
    st = st.split(', ')
    dct = {el.split("=")[0]:int(el.split("=")[1]) for el in st}
    return dct