# https://www.codewars.com/kata/55ca43fb05c5f2f97f0000fd
def list_animals(animals):
    return "".join([f"{i+1}. {el}\n" for i, el in enumerate(animals)])