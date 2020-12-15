https://www.codewars.com/kata/588fe9eaadbbfb44b70001fc
import string
def read_zalgo(zalgotext):
    s = string.digits + string.punctuation + string.ascii_letters + ' '
    return "".join([el for el in zalgotext if el in s])