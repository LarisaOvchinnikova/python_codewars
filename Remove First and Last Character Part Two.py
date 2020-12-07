# https://www.codewars.com/kata/570597e258b58f6edc00230d/train/python
def array(s):
    arr = s.replace(" ", "").split(",")
    return None if len(arr) <= 2 else " ".join(arr[1:-1])