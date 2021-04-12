# https://www.codewars.com/kata/55b95c76e08bd5eef100001e
def count_arara(n):
    pairs = n // 2
    ones = n % 2
    return  ('adak ' * pairs + 'anane' * ones).strip()