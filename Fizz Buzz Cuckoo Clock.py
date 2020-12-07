https://www.codewars.com/kata/58485a43d750d23bad0000e6
def fizz_buzz_cuckoo_clock(time):
    hour, minutes = [int(el) for el in time.split(":")]
    if hour >= 13:
        hour = hour - 12
    ans = []
    if minutes == 0:
        return (hour * "Cuckoo ")[:-1] if hour > 0 else (12 * "Cuckoo ")[:-1]
    if minutes == 30:
        return "Cuckoo"
    if minutes % 3 == 0:
        ans.append("Fizz")
    if minutes % 5 == 0:
        ans.append("Buzz")
    return "tick" if ans == [] else " ".join(ans)