# https://www.codewars.com/kata/57d1f36705c186d018000813
def gordon(a):
    a = a.upper().split(' ')
    return " ".join(
        [el.replace("A", '@').replace("O", "*").replace("U", "*").replace("I", "*").replace("E", "*") + "!!!!" for el in
         a])
