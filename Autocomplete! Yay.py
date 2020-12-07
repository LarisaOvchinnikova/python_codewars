# https://www.codewars.com/kata/5389864ec72ce03383000484/train/python
def autocomplete(input_, dictionary):
    input = "".join([el for el in input_ if el.isalpha()])
    return [el for el in dictionary if (el.lower()).startswith(input.lower())][:5]