https://www.codewars.com/kata/583ade15666df5a64e000058
def evens_and_odds(n):
    return bin(n)[2:] if n % 2 == 0 else hex(n)[2:]