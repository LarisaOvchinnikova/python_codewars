https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3
def abbrevName(name):
    name = name.upper()
    return f"{name[0]}.{name[name.index(' ') + 1]}"