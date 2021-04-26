# https://www.codewars.com/kata/5c44b0b200ce187106452139
def args_count(*args, **kwargs):
    return len(args) + len(kwargs)