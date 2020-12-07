# https://www.codewars.com/kata/5839edaa6754d6fec10000a2
def find_missing_letter(chars):
    lst_full = list(range(ord(chars[0]), ord(chars[-1])+1))
    lst_chars = [ord(char) for char in chars]
    set_full = set(lst_full)
    set_chars = set(lst_chars)
    return chr(list(set_full - set_chars)[0])

print(find_missing_letter(['a','b','c','d','f']))

# --2 case
def find_missing_letter(chars):
    lst_full = list(range(ord(chars[0]), ord(chars[-1])+1))
    lst_chars = [ord(char) for char in chars]
    return [chr(el) for el in lst_full if not el in lst_chars][0]
