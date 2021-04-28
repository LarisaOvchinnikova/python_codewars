# https://www.codewars.com/kata/5b043e3886d0752685000009
def michael_pays(costs):
    return round(costs,2) if costs < 5 else round(costs*2/3,2) if costs/3<=10 else round(costs-10,2)