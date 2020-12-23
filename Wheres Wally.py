# https://www.codewars.com/kata/55f91a98db47502cfc00001b
import re
def wheres_wally(string):
    string = " " + string
    return -1 if re.search(r' Wally\b', string) == None else string.find(" Wally")