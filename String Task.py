# https://www.codewars.com/kata/598ab63c7367483c890000f4
def string_task(s):
    return "".join(["." + el.lower() for el in s if el.lower() not in "aeyuio"])