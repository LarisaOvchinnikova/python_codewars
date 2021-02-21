# https://www.codewars.com/kata/5856c5f7f37aeceaa100008e
def baubles_on_tree(baubles, branches):
    if branches == 0:
        return "Grandma, we will have to buy a Christmas tree first!"
    bubl = baubles // branches
    arr = [bubl] * branches
    rest = baubles % branches
    for i in range(branches):
        if i < rest:
            arr[i] += 1
    return arr