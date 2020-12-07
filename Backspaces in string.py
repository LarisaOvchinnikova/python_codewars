# https://www.codewars.com/kata/5727bb0fe81185ae62000ae3/solutions/python
def clean_string(s):
    result = []
    for letter in s:
        if letter != '#':
            result.append(letter)
        elif len(result) > 0:
            result.pop()
    return "".join(result)