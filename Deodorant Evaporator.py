https://www.codewars.com/kata/5506b230a11c0aeab3000c1f

def evaporator(content, evap_per_day, threshold):
    n = 0
    limit = content * threshold/100
    while content > limit:
        content = content - content * evap_per_day/100
        n += 1
    return n