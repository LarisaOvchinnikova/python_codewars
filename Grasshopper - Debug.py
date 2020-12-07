# https://www.codewars.com/kata/55cb854deb36f11f130000e1
def weather_info(temp):
    c = convertToCelsius(temp)
    if c < 0:
        return f"{c} is freezing temperature"
    else:
        return f"{c} is above freezing temperature"


def convertToCelsius(temp):
    celsius = (temp - 32) * (5 / 9)
    return celsius