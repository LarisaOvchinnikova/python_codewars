https://www.codewars.com/kata/59e19a747905df23cb000024
def string_letter_count(s):
    s = s.lower()
    s1 = sorted(set([el for el in s if el.isalpha()]))
    return "".join([str(s.count(el))+el for el in s1])