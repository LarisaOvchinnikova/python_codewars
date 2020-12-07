https://www.codewars.com/kata/546274b0eaa31f79c9000d5d
def isAnagram(test, original):
    test = test.lower()
    original = original.lower()
    test = sorted([el for el in test if el.isalnum()])
    original = sorted([el for el in original if el.isalnum()])
    return test == original