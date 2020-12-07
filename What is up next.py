https://www.codewars.com/kata/542ebbdb494db239f8000046
def next_item(xs, item):
    is_found = False
    for el in xs:
        if is_found:
            return el
        if el == item:
            is_found = True
    return None