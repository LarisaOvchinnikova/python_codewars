# https://www.codewars.com/kata/529eef7a9194e0cbc1000255/train/python
def is_anagram(test, original):
    return "".join(sorted(test.lower())) == "".join(sorted(original.lower()))