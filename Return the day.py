https://www.codewars.com/kata/59dd3ccdded72fc78b000b25
def whatday(num):
    return { 1: 'Sunday', 2: 'Monday', 3: 'Tuesday',
             4: 'Wednesday', 5: 'Thursday', 6: 'Friday',
             7: "Saturday" }[num] if num in [1,2,3,4,5,6,7] else 'Wrong, please enter a number between 1 and 7'