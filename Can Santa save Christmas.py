#https://www.codewars.com/kata/5857e8bb9948644aa1000246
def determine_time(arr):
    times = [el.split(":") for el in arr]
    return sum([int(el[0])*3600 + int(el[1])*60 + int(el[2]) for el in times]) < 24*3600