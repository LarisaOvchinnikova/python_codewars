# https://www.codewars.com/kata/5b16490986b6d336c900007d/train/python

def my_languages(results):
    res = {value: key for key, value in results.items() if value >= 60}
    arr = sorted(res.keys(), reverse = True)
    return [res[value] for value in arr]