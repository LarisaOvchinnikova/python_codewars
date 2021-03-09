# https://www.codewars.com/kata/53da6a7e112bd15cbc000012
def sort_dict(d):
    return sorted(d.items(), key=lambda el: el[1], reverse=True)