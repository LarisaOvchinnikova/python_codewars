https://www.codewars.com/kata/57ecf6efc7fe13eb070000e1/
def outed(meet, boss):
    s = meet[boss]
    for name in meet:
        s+= meet[name]
    n = len(list(meet.keys()))
    return 'Get Out Now!' if s / n <= 5 else 'Nice Work Champ!'

# 2 case
def outed(meet, boss):
    return 'Get Out Now!' if (sum(meet.values()) + meet[boss]) / len(meet.values()) <= 5 else 'Nice Work Champ!'