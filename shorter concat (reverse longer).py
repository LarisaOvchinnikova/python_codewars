# https://www.codewars.com/kata/54557d61126a00423b000a45
def shorter_reverse_longer(a,b):
    return a + b[::-1] + a if len(a) < len(b) else b + a[::-1] + b

# 2 case
def switch_it_up(number):
    return ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'][number]