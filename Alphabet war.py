# https://www.codewars.com/kata/59377c53e66267c8f6000027
def alphabet_war(fight):
    left = {"w":4, "p":3, "b":2, "s":1}
    right = {"m":4, "q":3, "d":2, "z":1}
    sl, sr = 0, 0
    for el in fight:
        if el in left:
            sl += left[el]
        if el in right:
            sr += right[el]
    return "Right side wins!" if sr > sl else "Left side wins!" if sl > sr else "Let's fight again!"
