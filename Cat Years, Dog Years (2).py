# https://www.codewars.com/kata/5a6d3bd238f80014a2000187
def owned_cat_and_dog(cat_years, dog_years):
    if cat_years < 15:
        cat = 0
    elif cat_years < 24:
        cat = 1
    else:
        cat = 2 + (cat_years - 24) // 4

    if dog_years < 15:
        dog = 0
    elif dog_years < 24:
        dog = 1
    else:
        dog = 2 + (dog_years - 24) // 5
    return [cat, dog]

# 2 case
def owned_cat_and_dog(cy, dy):
    cat = 0 if cy < 15 else 1 if cy < 24 else 2 + (cy - 24) // 4
    dog = 0 if dy < 15 else 1 if dy < 24 else 2 + (dy - 24) // 5
    return [cat, dog]