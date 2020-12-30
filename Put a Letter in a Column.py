# https://www.codewars.com/kata/563d54a7329a7af8f4000059
def build_row_text(i, character):
    arr = ["| "] * 9
    arr[i] = "|"+character
    return "".join(arr)+"|"