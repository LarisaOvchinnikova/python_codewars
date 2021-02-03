from datetime import date

def age_in_days(year, month, day):
    days = (date.today() - date(year, month, day)).days
    return f"You are {days} days old"

print(age_in_days(1960, 4, 27))