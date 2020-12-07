https://www.codewars.com/kata/5e4ee2c17770f20016d52f60
def sort_by_num(s):
    s1 = ""
    for el in s:
        if el.isdigit():
            s1 += el + " "
        else:
            s1 += el
    arr = s1.split()
    arr = sorted(arr, key=lambda el:el[1])
    return "".join(arr)

# 2 case
def sort_by_num(s):
    arr = [s[i]+s[i+1] for i in range(0, len(s), 2)]
    return "".join(sorted(arr, key=lambda el:el[1]))