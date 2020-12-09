# https://www.codewars.com/kata/536c00e21da4dc0a0700128b
from datetime import datetime
def get_villain_name(birthdate):
    day = birthdate.day % 10
    m = birthdate.month
    first = [ "The Evil","The Vile","The Cruel", "The Trashy","The Despicable", "The Embarrassing", "The Disreputable","The Atrocious", "The Twirling",  "The Orange","The Terrifying", "The Awkward"]
    last = ["Mustache", "Pickle", "Hood Ornament", "Raisin", "Recycling Bin", "Potato", "Tomato", "House Cat", "Teaspoon", "Laundry Basket"]
    name = first[m - 1] +  " " + last[day]
    return name