# https://www.codewars.com/kata/5981a139f5471fd1b2000071
def task(w,n,c):
    names = {'Monday':'James',
             'Tuesday':'John',
             'Wednesday': 'Robert',
             'Thursday':'Michael',
             'Friday':'William'}
    return f'It is {w} today, {names[w]}, you have to work, you must spray {n} trees and you need {n*c} dollars to buy liquid'
