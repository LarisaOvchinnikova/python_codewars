# https://www.codewars.com/kata/557efeb04effce569d000022
def make_acronym(phrase):
    if type(phrase) != str:
        return 'Not a string'
    elif phrase == "":
        return ""
    elif phrase.replace(" ","").isalpha():
        return "".join([el[0] for el in phrase.upper().split()])
    else:
        return 'Not letters'