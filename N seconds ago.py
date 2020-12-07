#https://www.codewars.com/kata/5a631508e626c5f127000055/train/python

from datetime import datetime, timedelta
def seconds_ago(s,n):
    time = datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
    print(time)
    return time - timedelta(seconds=n)



print(seconds_ago('2000-01-01 00:00:00',1))
print(seconds_ago('0001-02-03 04:05:06',7))

# from datetime import datetime, timedelta
# def seconds_ago(s,n):
#     time = datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
#     res = (time - timedelta(seconds=n)).strftime("%Y-%m-%d %H:%M:%S")
#     y = res.split("-")[0]
#     if len(y) < 4:
#         res = "0"* (4-len(y)) + res
#     return res