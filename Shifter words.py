# https://www.codewars.com/kata/603b2bb1c7646d000f900083
def shifter(st):
    shifters = set("HINOSXZMW")
    count = 0
    arr = set(st.split())
    for el in arr:
        if set(el) == set(el) & shifters:
            count += 1
    return count