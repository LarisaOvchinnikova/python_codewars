# https://www.codewars.com/kata/554ca54ffa7d91b236000023
def delete_nth(order,max_e):
    arr = []
    for el in order:
        if arr.count(el) < max_e:
            arr.append(el)
    return arr