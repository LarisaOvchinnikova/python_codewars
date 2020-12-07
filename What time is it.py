# https://www.codewars.com/kata/57729a09914da60e17000329/train/python
from datetime import datetime
def get_military_time(time_12):
    time = datetime.strptime(time_12, "%I:%M:%S%p")
    time_24 = time.strftime("%H:%M:%S")
    return time_24