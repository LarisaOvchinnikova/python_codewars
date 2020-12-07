https://www.codewars.com/kata/557af4c6169ac832300000ba
def remove_rotten(bag_of_fruits):
    return [el.lower().replace("rotten", "") for el in bag_of_fruits] if bag_of_fruits else []