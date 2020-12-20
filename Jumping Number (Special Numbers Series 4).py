# https://www.codewars.com/kata/5a54e796b3bfa8932c0000ed
def jumping_number(num):
    s = [int(el) for el in str(num)]
    arr = [True if abs(s[i] - s[i+1]) == 1 else False for i in range(len(s)-1)]
    return "Jumping!!" if all(arr) else "Not!!"