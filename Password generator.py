# https://www.codewars.com/kata/58ade2233c9736b01d0000b3
import string
from random import randint, choice
def password_gen():
    s1 = string.digits
    s2 = string.ascii_lowercase
    s3 = string.ascii_uppercase
    l = randint(6,20)
    password = choice(s2) + choice(s1) + choice(s3)
    while len(password) < l:
        password += choice(s1+s2+s3)
    return password