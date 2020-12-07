# https://www.codewars.com/kata/57a429e253ba3381850000fb
def bmi(weight, height):
    bmi = weight/height**2
    if bmi <= 18.5:
        return 'Underweight'
    elif bmi <= 25:
       return 'Normal'
    elif bmi <= 30:
        return 'Overweight'
    else:
        return 'Obese'