# https://www.codewars.com/kata/599bb194b7a047b04d000077
def how_many_pizzas(n):
    s_1 = n ** 2
    s_8 = 64
    pizzas = s_1 // s_8
    slices = (s_1 % s_8) // 8
    return f"pizzas: {pizzas}, slices: {slices}"