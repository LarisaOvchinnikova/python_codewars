# https://www.codewars.com/kata/59b0a6da44a4b7080300008a
def to24hourtime(hour, minute, period):
    if period == "am" and hour == 12:
        hour = 0
    if period == "pm" and hour != 12:
        hour = hour + 12
    minute = str(minute).rjust(2, "0")
    hour = str(hour).rjust(2, "0")
    return hour + minute