# https://www.codewars.com/kata/57f6051c3ff02f3b7300008b
def meeting(rooms, need):
    if need == 0: return 'Game On'
    arr = []
    rest = need
    for el in rooms:
        if rest > 0:
            chairs = el[1] - len(el[0])
            if chairs > 0:
                arr.append(chairs) if chairs < rest else arr.append(rest)
            else:
                arr.append(0)
            if chairs > 0: rest -= chairs
        else: return arr
    return  arr if rest <= 0 else 'Not enough!'