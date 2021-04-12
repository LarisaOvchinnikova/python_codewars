# https://www.codewars.com/kata/57ebdf1c2d45a0ecd7002cd5
def inside_out(st):
    st = st.split(' ')
    arr = []
    for el in st:
        mid = len(el) // 2
        if len(el) % 2 == 0:
            arr.append(el[:mid][::-1] + el[mid:][::-1])
        else:
            arr.append(el[:mid][::-1] + el[mid] + el[mid+1:][::-1])
    return " ".join(arr)