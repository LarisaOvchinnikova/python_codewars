# https://www.codewars.com/kata/55de9c184bb732a87f000055
def reverse(seq):
    for i in range(len(seq)//2):
        seq[i], seq[len(seq)-1-i] = seq[len(seq)-1-i], seq[i]