https://www.codewars.com/kata/55736129f78b30311300010f
def pattern(n):
    return "\n".join(["".join(map(str,list(range(i,n+1)))) for i in range(1, n+1)])