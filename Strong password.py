# https://www.codewars.com/kata/57e35f1bc763b8ccce000038
import string
def check_password(s):
    s1 = 8 <= len(s) <= 20
    s2 = len([el for el in s if el in string.ascii_uppercase]) > 0
    s3 = len([el for el in s if el in string.ascii_lowercase]) > 0
    s4 = len([el for el in s if el.isdigit()]) > 0
    s5 = len([el for el in s if el in "!@#$%^&*?"]) > 0
    s6 =  len([el for el in s if el not in string.ascii_letters + string.digits + "!@#$%^&*?"])==0
    return "valid" if s1 and s2 and s3 and s4 and s5 and s6 else "not valid"