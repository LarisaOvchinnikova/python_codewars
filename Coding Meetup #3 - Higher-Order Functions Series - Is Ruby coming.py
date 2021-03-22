# https://www.codewars.com/kata/5827acd5f524dd029d0005a4
def is_ruby_coming(lst):
    return [el for el in lst if el["language"] == "Ruby"] != []