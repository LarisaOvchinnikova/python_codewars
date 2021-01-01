# https://www.codewars.com/kata/57a23c2acf1fa514d0001034
def who_took_the_car_key(message):
    return "".join([chr(int(el, 2)) for el in message])