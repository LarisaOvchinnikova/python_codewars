# https://www.codewars.com/kata/59759761e30a19cfe1000024
def aa_percentage(st, lst=["A", "I", "L", "M", "F", "W", "Y", "V"]):
    return round(sum([st.count(el) for el in lst]) / len(st) * 100)