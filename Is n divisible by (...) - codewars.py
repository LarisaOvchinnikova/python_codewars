https://www.codewars.com/kata/558ee8415872565824000007
def is_divisible(*args):
    return len([el for el in args if args[0] % el == 0]) == len(args)