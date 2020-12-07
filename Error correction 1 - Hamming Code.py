#https://www.codewars.com/kata/5ef9ca8b76be6d001d5e1c3e
def encode(string):
    s = "".join([bin(ord(el))[2:].rjust(8, "0") for el in string])
    return "".join([el * 3 for el in s])


def decode(bits):
    triades = [bits[i:i + 3] for i in range(0, len(bits), 3)]
    for i in range(len(triades)):
        if triades[i].count("1") == 3:
            triades[i] = "1"
        elif triades[i].count("0") == 3:
            triades[i] = "0"
        if triades[i].count("1") == 2:
            triades[i] = "1"
        elif triades[i].count("0") == 2:
            triades[i] = "0"
    bin_code = "".join(triades)
    octes = [bin_code[i:i + 8] for i in range(0, len(bin_code), 8)]
    return "".join([chr(int(el, 2)) for el in octes])