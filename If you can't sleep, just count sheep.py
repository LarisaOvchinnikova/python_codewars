# If you can't sleep, just count sheep!!
# https://www.codewars.com/kata/5b077ebdaf15be5c7f000077

def count_sheep(n):
    s = ''
    i = 1
    while i <= n:
        s = s + str(i) + " sheep..."
        i = i + 1
    return s

# -- 2 case---
# If you can't sleep, just count sheep!!
def count_sheep(n):
    s = ""
    for i in range (1, n+1):
        s = s + f"{i} sheep..."
    return s

# --- 3 case ---
def count_sheep(n):
    lst = [(str(i) + " sheep") for i in range(1, n+1)]
    return "...".join(lst) + "..."