# https://www.codewars.com/kata/5b23d98da97f02a5f4000a4c
def dollar_to_speech(v):
    v = v.replace("$", "").split(".")
    if v[0][0] == '-':
        return 'No negative numbers are allowed!'
    if v[0] == '1' and v[1] == '00':
        return f'{v[0]} dollar.'
    if v[1] == '00':
        return f'{v[0]} dollars.'
    if v[0] == '0' and v[1] == '01':
        return '1 cent.'
    if v[1] == '01':
        return f'{v[0]} dollars and 1 cent.'
    if v[0] == '0' and v[1] != '01':
        return f'{v[1]} cents.'
    if v[1] <= '09':
        return f'{v[0]} dollars and {v[1][1]} cents.'
    return f'{v[0]} dollars and {v[1]} cents.'