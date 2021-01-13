# https://www.codewars.com/kata/54599705cbae2aa60b0011a4
def one(sq, fun):
    return len([el for el in sq if fun(el)]) == 1