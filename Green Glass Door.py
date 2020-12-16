# https://www.codewars.com/kata/5642bf07a586135a6f000004
def step_through_with(s):
    return [s[i] for i in range(len(s)-1) if s[i] == s[i+1]] != []