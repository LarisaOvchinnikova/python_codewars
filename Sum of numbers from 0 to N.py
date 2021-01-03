# https://www.codewars.com/kata/56e9e4f516bcaa8d4f001763
def show_sequence(n):
    s = sum(list(range(n+1)))
    st = "+".join([str(i) for i in range(n+1)])
    return f"{st} = {s}" if s > 0 else "0=0" if n == 0 else f"{n}<0"