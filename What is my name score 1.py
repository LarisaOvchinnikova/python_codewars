https://www.codewars.com/kata/576a29ab726f4bba4b000bb1
def name_score(name):
    # alpha = {'ABCDE':1,'FGHIJ':2,'KLMNO':3,'PQRST':4,'UVWXY':5}
    # #this is random dictionary in tests
    s = 0
    res = {}
    for letter in name:
        for key in alpha:
            if letter.upper() in key:
                s+=alpha[key]
    res[name] = s
    return res