# https://www.codewars.com/kata/52cd53948d673a6e66000576
def search(titles, term):
    return [el for el in titles if term.lower() in el.lower()]