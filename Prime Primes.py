https://www.codewars.com/kata/57ba58d68dcd97e98c00012b
def is_prime(n):
    if n <= 1: return False
    for i in range(2, round(n**0.5)+1):
        if n % i == 0: return False
    return True

def prime_primes(n):
    arr = [x for x in range(2, n) if is_prime(x)]
    s = 0
    count = 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            s += arr[i]/arr[j]
            count+=1
    return count, int(s)