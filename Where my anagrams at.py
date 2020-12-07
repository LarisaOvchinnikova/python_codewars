def anagrams(word, words):
    match = {}
    for char in word:
        match[char] = word.count(char)
    print(match)
    res = []
    for w in words:
        dct = {}
        for letter in w:
            dct[letter] = w.count(letter)
        if match == dct:
            res.append(w)
    return res