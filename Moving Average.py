https://www.codewars.com/kata/5c745b30f6216a301dc4dda5/train/python
def moving_average(values,n):
    if n==0 or n>len(values):
        return None
    return [sum(values[i:i+n])/n for i in range(len(values)+1-n)]