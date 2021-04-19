# https://www.codewars.com/kata/5a40c250c5e284a76400008c
def bouncing_ball(initial, proportion):
    count = 0
    while initial > 1:
        initial *= proportion
        count += 1
    return count
