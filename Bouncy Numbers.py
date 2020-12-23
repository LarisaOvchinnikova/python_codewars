# https://www.codewars.com/kata/5769a78c6f2dea72b3000027
def is_bouncy(num):
    s = str(num)
    if len(s) < 3: return False
    if s == "".join(sorted(s)) or s == "".join(sorted(s, reverse=True)):
        return False
    else:
        return True