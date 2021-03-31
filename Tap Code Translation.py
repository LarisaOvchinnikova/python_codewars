# https://www.codewars.com/kata/605f5d33f38ca800322cb18f
def tap_code_translation(text):
    text = text.upper().replace("C", "K")
    a = [["A", "B", "K", "D", "E",],
         ["F", "G", "H",  "I", "J"],
         ["L", "M", "N",  "O", "P"],
         ["Q", "R", "S",  "T", "U"],
         ["V", "W", "X",  "Y", "Z"]
        ]
    s = []
    for el in text:
        for i,row in enumerate(a):
            if el in row:
                x = i
                y = row.index(el)
        s.append("." * (x+1) + " " + "." * (y+1))
    return ' '.join(s)