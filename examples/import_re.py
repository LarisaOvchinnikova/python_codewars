import re
def cinema(x, y):
    if x > 2 * y or y > 2 * x: return None
    return 'BGB'* (x - y) + 'BG' * (2 * y - x) if x >= y else 'GBG'* (y - x) + 'GB' * (2 * x - y)

def check(x, y, expected):
    if type(expected) == str:
        expected = [expected]
    actual = cinema(x, y)
    msg = ', '.join(expected)
    if "," in msg:
        coma = msg.rindex(",")
        msg = msg[:coma]+ " or" + msg[coma+1:]
    # msg = re.sub(r', [^,]+$', ' or ', msg)  # quite cumbersome, but this is to keep your current output format
    # test.expect(actual in exp, f'expected {msg}, but received {actual}')
    if actual in expected:
        t = f'expected {msg}, received {actual}'
    else:
        t = f'expected {msg}, but received {actual}'
    return t

print(check(2, 2, ["BGBG", "GBGB", "BGGB", "GBBG"]))
print(check(1, 1, "BG"))
print(check(1, 2, "GBG"))
print(check(3, 2, ["BGBBG", "BGBGB", "GBBGB", "BGBGB"]))