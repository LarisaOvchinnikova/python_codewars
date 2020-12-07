https://www.codewars.com/kata/5848cd33c3689be0dc00175c
def add(s1, s2):
    s1 = sum([ord(el) for el in s1])
    s2 = sum([ord(el) for el in s2])
    return s1 + s2