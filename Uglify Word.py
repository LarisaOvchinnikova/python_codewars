https://www.codewars.com/kata/5ce6cf94cb83dc0020da1929
def uglify_word(s):
    a = ""
    i = 0
    for el in s:
        if el.isalpha():
            if i % 2==0:
                a += el.upper()
            elif i % 2 == 1:
                 a += el.lower()
            i += 1
        else:
            i = 0
            a += el
    return a