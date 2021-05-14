# https://www.codewars.com/kata/515decfd9dcfc23bb6000006
def is_valid_IP(s):
    s = s.split('.')
    if len(s)!= 4: return False
    return len([el for el in s if el.isdigit() and (len(el) == 1 or len(el) > 1 and el[0]!= '0') and 0<=int(el)<=255])==4