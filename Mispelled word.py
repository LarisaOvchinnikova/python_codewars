# https://www.codewars.com/kata/5892595f190ca40ad0000095
def mispelled(word1,word2):
    if word1 == word2 or word1 in word2 and len(word1)+1 == len(word2) or word2 in word1 and len(word2) + 1 == len(word1):
        return True
    if len(word1) != len(word2): return False
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    return count <= 1