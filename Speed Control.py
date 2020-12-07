# https://www.codewars.com/kata/56484848ba95170a8000004d/train/python
def gps(s, x):
    if len(x) <= 1:
        return 0
    distances = [abs(x[i] - x [i - 1]) for i in range(1,len(x))]
    hours = s/3600
    speed  = [dist/hours for dist in distances]
    return max(speed)