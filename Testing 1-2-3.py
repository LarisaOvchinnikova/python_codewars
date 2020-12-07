https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9/train/python
def number(lines):
    return [f"{str(i+1)}: {el}" for i, el in enumerate(lines)]