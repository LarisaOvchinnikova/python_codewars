# https://www.codewars.com/kata/5772ded6914da62b4b0000f8
def palindrome_pairs(words):
    res = []
    words = [str(el) for el in words]
    for i in range(len(words)):
        for j in range(len(words)):
            if words[i] + words[j] == (words[i] + words[j])[::-1]  and i != j:
                res.append([i, j])
    return res