# https://www.codewars.com/kata/56a32dd6e4f4748cc3000006
def mean(town, st):
    s = st.split("\n")
    strng = ''
    for el in s:
        c = el.index(":")
        city = el[:c]
        if city == town:
            strng = el[c+1:]
            break
    if strng == '': return -1
    s = strng.split(',')
    rain = [float(el.split(" ")[1]) for el in s]
    av = sum(rain) / len(rain)
    return av
def variance(town, st):
    s = st.split("\n")
    strng = ''
    for el in s:
        c = el.index(":")
        city = el[:c]
        if city == town:
            strng = el[c+1:]
            break
    if strng == '': return -1
    s = strng.split(',')
    rain = [float(el.split(" ")[1]) for el in s]
    av = sum(rain) / len(rain)
    res = [(el - av)** 2 for el in rain]
    res = sum(res) / len(res)
    return res