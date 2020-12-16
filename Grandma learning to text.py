# https://www.codewars.com/kata/5a043fbef3251a5a2b0002b0
import re
def textin(st):
    return re.sub(r'(two|too|to)', '2', st, flags=re.I)

# 2 case
import re
def textin(st):
    st = re.sub("too", "2", st, flags=re.IGNORECASE)
    st = re.sub("to", "2", st, flags=re.IGNORECASE)
    st = re.sub("two", "2", st, flags=re.IGNORECASE)
    return st