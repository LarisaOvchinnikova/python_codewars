# https://www.codewars.com/kata/57e2afb6e108c01da000026e
def expression_out(exp):
    print(exp)
    exp = exp.split(" ")
    op = {
      '+':   'Plus ',
      '-':   'Minus ',
      '*':   'Times ',
      '/':   'Divided By ',
      '**':  'To The Power Of ',
      '=':   'Equals ',
      '!=':  'Does Not Equal '}
    if exp[1] not in op: return "That's not an operator!"
    num = {
      '0': 'Zero',
      '1': 'One',
      '2': 'Two',
      '3': 'Three',
      '4': 'Four',
      '5': 'Five',
      '6': 'Six',
      '7': 'Seven',
      '8': 'Eight',
      '9': 'Nine' ,
      '10': 'Ten',
    }
    return f"{num[exp[0]]} {op[exp[1]]}{num[exp[2]]}"