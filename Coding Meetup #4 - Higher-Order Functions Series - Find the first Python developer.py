# https://www.codewars.com/kata/5827bc50f524dd029d0005f2
def get_first_python(users):
    p = [f"{el['first_name']}, {el['country']}" for el in users if el['language'] == "Python"]
    return p[0]  if p != [] else 'There will be no Python developers'