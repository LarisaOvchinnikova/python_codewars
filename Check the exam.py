# https://www.codewars.com/kata/5a3dd29055519e23ec000074/train/python
def check_exam(arr1,arr2):
    score = 0
    for i in range (len(arr1)):
        if arr1[i] == arr2[i]:
            score+=4
        elif arr2[i] == "":
            score = score
        else:
            score -= 1
    return score if score > 0 else 0