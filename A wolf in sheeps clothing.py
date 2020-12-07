https://www.codewars.com/kata/5c8bfa44b9d1192e1ebd3d15
def warn_the_sheep(queue):
    queue =  queue[::-1]
    wolf = queue.index('wolf')
    if wolf  == 0:
        return 'Pls go away and stop eating my sheep'
    else:
        return f"Oi! Sheep number {wolf}! You are about to be eaten by a wolf!"