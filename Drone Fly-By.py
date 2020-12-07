# https://www.codewars.com/kata/58356a94f8358058f30004b5/train/python
def fly_by(lamps, drone):
    return "o"* len(lamps) if len(lamps) <= len(drone) else "o" * len(drone) + "x" * (len(lamps) - len(drone))