https://www.codewars.com/kata/5ae62fcf252e66d44d00008e

def expression_matter(a, b, c):
    d1 = a+b+c
    d2 = a*(b+c)
    d3 = a*b*c
    d4 = a+b*c
    d5 = (a+b)*c
    return max(d1,d2,d3,d4,d5)