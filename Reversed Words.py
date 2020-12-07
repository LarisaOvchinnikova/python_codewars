# https://www.codewars.com/kata/51c8991dee245d7ddf00000e
def reverseWords(str):
    lst = str.split()
    return " ".join(lst[::-1])