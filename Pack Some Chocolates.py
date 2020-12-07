https://www.codewars.com/kata/5f5daf1a209a64001183af9b
def make_chocolates(small, big, goal):
    for s in range(small + 1):
        for b in range(big + 1):
            if b * 5 + s * 2 == goal:
                return s
    return -1