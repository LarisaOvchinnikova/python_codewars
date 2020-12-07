https://www.codewars.com/kata/57ee4a67108d3fd9eb0000e7
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

def goose_filter(birds):
    return [el for el in birds if not el in geese]