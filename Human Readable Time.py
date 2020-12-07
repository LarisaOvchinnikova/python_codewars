#https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python
def make_readable(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    sec = seconds % 3600 % 60
    time = [hours, minutes, sec]
    return ":".join([str(el).rjust(2, "0") for el in time])