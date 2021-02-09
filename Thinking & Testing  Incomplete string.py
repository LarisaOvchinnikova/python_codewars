# https://www.codewars.com/kata/56d9292cc11bcc3629000533
def testit(s):
    arr = [chr((ord(s[i]) + ord(s[i+1]))//2) for i in range(0,len(s)-1,2)]
    return "".join(arr) if len(s) % 2 == 0 else "".join(arr) + s[-1]