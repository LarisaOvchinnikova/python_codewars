# https://www.codewars.com/kata/5862f663b4e9d6f12b00003b
def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    count = blue_start + red_start
    remain_total = count - blue_pulled - red_pulled
    remain_blue = blue_start - blue_pulled
    probability = remain_blue / remain_total
    return probability