# https://www.codewars.com/kata/597d75744f4190857a00008d
def paint_letterboxes(start, finish):
    s = "".join([str(i) for i in range(start, finish+1)])
    return [s.count(el) for el in '0123456789']