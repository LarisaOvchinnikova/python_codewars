# https://www.codewars.com/kata/59b0ab12cf3395ef68000081
def to12hourtime(timestring):
    h , mm = int(timestring[:2]),timestring[2:]
    if h > 12:
        h = h - 12
        return f'{h}:{mm} pm'
    elif h == 12:
        return f'{h}:{mm} pm'
    elif h == 0:
        return f'{12}:{mm} am'
    else:
        return f'{h}:{mm} am'

# 2 case
from datetime import datetime
def to12hourtime(timestring):
    return datetime.strptime(timestring, '%H%M').strftime('%-I:%M %p').lower()

# 3 case
from datetime import datetime
def to12hourtime(t):
    return datetime.strptime(t,'%H%M').strftime('%I:%M %p').lstrip('0').lower()