# https://www.codewars.com/kata/586538146b56991861000293
def to_nato(words):
    words = words.lower().replace(" ", "")
    dct = {"a":"Alfa", "b":"Bravo", "c":"Charlie", "d":"Delta", "e":"Echo",
           "f":"Foxtrot", "g":"Golf", "h":"Hotel", "i":"India", "j":"Juliett",
           "k":"Kilo", "l":"Lima", "m":"Mike", "n":"November", "o":"Oscar",
           "p":"Papa", "q":"Quebec", "r":"Romeo", "s":"Sierra", "t":"Tango",
           "u":"Uniform", "v":"Victor", "w":"Whiskey", "x":"Xray", "y":"Yankee", "z":"Zulu"}
    return " ".join([dct[el] if el in dct else el for el in words])