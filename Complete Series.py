https://www.codewars.com/kata/580a4001d6df740d61000301
def complete_series(seq):
    return list(range(0, max(seq)+1)) if len(set(seq)) == len(seq) else [0]