https://www.codewars.com/kata/56d46b8fda159582e100001b/solutions/python
def travel(total_time, run_time, rest_time, speed):
    parts = total_time // (run_time + rest_time)
    rem = total_time % (run_time + rest_time)
    if rem >= run_time:
        return parts * (speed * run_time) + run_time * speed
    else:
        return parts * (speed * run_time) + rem * speed