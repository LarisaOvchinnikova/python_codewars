https://www.codewars.com/kata/554e4a2f232cdd87d9000038
# def DNA_strand(dna):
#     return dna.replace("A", "t")\
#               .replace("T", "a")\
#               .replace("C", "g")\
#               .replace("G", "c").upper()

def DNA_strand(dna):
    dct = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }
    return "".join([dct[letter] for letter in dna])