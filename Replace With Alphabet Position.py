#https://www.codewars.com/kata/546f922b54af40e1e90001da
def alphabet_position(text):
    text = text.lower()
    return " ".join([str(ord(c) - 96) for c in text if c.isalpha()])

#2 case

def alphabet_position(text):
    alph = " abcdefghijklmnopqrstuvwxyz"
    return " ".join([str(alph.index(el)) for el in text.lower() if el.isalpha()])