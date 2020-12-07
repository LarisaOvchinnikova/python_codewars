# https://www.codewars.com/kata/5761a717780f8950ce001473
def calculate_age(year_of_birth, current_year):
    r = current_year - year_of_birth
    if r < -1:
        return f"You will be born in {-r} years."
    elif r == -1:
        return f"You will be born in {-r} year."
    elif r == 0:
        return 'You were born this very year!'
    elif r == 1:
        return f"You are {r} year old."
    else:
        return f"You are {r} years old."