# https://www.codewars.com/kata/517abf86da9663f1d2000003
def to_camel_case(text):
    if text == "":
        return ""
    new_text = text.replace('-', ' ').replace('_', ' ').split(" ")

    return "".join([el.title() if i > 0 else el for i, el in enumerate(new_text)])