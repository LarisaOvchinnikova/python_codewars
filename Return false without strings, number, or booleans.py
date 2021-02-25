# https://www.codewars.com/kata/603447245a5898001c0c0c14
def return_false():
    one = len([[]])
    two = one + one
    five = one + two * two
    six = five + one
    seven = six + one
    eight = seven + one
    nine = eight + one
    ten = nine + one
    hundred = ten * ten
    return eval(chr(ten * seven) + chr(ten * nine + seven) + chr(hundred+ eight) + chr(hundred + ten + five) + chr(hundred + one))