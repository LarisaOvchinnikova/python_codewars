# Tally it up
# # https://www.codewars.com/kata/5630d1747935943168000013

def score_to_tally(score):
    l = 'abcde'
    fives = score // 5
    rest = score % 5
    return "e <br>" * fives + (l[rest-1] if rest > 0 else "")