https://www.codewars.com/kata/57829376a1b8d576640000d6
def trump_detector(trump):
    lst = "".join(list(trump.lower().split()))
    res = lst[0]
    for i in range(1,len(lst)):
        if lst[i] != res[-1]:
            res += " " + lst[i]
        else:
            res += lst[i]
    arr = [el for el in res.split(' ') if el[0] in "aeuio"]
    arr1 = [len(el)-1 for el in arr if len(el) > 0]
    return round(sum(arr1)/len(arr1), 2)