# https://www.codewars.com/kata/52b23340c65ea422b1000045
def will_fit(present, box):
    box = list(box)
    present = list(present)
    box.sort()
    present.sort()
    for i in range(3):
        if present[i] >= box[i]-1:
            return False
    return True