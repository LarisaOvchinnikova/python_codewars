# https://www.codewars.com/kata/5bc9951026f1cdc77400011c
def baby_count(x):
    x = x.lower()
    c = min(x.count("b")//2, x.count('a'), x.count("y"))
    return c if c > 0 else "Where's the baby?!"