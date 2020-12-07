# https://www.codewars.com/kata/57193694938fcdfe3a001dd7/train/python
def ipValidator(ip):
    if ip == "":
        return False
    ip = ip.split(".")
    if len(ip) != 4:
        return False
    res = [int(el) for el in ip if el.isdigit()]
    return len(res) == 4 and [0<=el<=255 for el in res].count(True) == 4