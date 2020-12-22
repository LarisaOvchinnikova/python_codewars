# https://www.codewars.com/kata/52b5247074ea613a09000164
import math
def cooking_time(eggs):
    parts = math.ceil(eggs / 8)
    return parts * 5