# https://www.codewars.com/kata/5355a811a93a501adf000ab7
def fizz_buzz_custom(string_one="Fizz", string_two="Buzz", num_one=3, num_two=5):
    res = []
    for i in range (1, 101):
        s = ""
        if i % num_one == 0:
            s+=string_one
        if i % num_two == 0:
            s+=string_two
        if s == "":
            res.append(i)
        else:
            res.append(s)
    return res