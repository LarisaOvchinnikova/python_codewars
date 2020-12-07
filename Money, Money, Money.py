https://www.codewars.com/kata/563f037412e5ada593000114/train/python
def calculate_years(money, interest, tax, desired):
    year = 0
    while money < desired:
        money = money + money * interest - money * interest * tax
        year += 1
    return year