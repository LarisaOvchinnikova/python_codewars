https://www.codewars.com/kata/544aed4c4a30184e960010f4/python
def divisors(n):
    res = []
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            res.append(i)
    if len(res) == 0:
        return f"{n} is prime"
    else:
        return res

# --- 2 case:
def divisors(n):
    return [i for i in range(2, n) if n % i == 0] or f"{n} is prime"