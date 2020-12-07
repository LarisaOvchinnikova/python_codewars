https://www.codewars.com/kata/5235c913397cbf2508000048
class Calculator(object):
    def evaluate(self, string):
        arr = string.split()
        if len(arr) == 1:
            arr = list(arr[0])
        for i in range(len(arr)):
            if len(arr[i])>1 and '(' in arr[i]:
                arr[i] = arr[i].replace('(','')
                arr.insert(i, "(")
            if len(arr[i])>1 and ')' in arr[i]:
                arr[i] = arr[i].replace(')','')
                arr.insert(i+1, ")")
        while ")" in arr:
            closeb= arr.index(")")
            for i in range(closeb-1, -1, -1):
                if arr[i] == "(":
                    openb = i
                    break
            part = arr[openb+1: closeb]
            if len(part) == 1:
                res = int(part[0])
            else:
                if "+" in part: res = int(part[0]) + int(part[2])
                if "-" in part: res = int(part[0]) - int(part[2])
                if "*" in part: res = int(part[0]) * int(part[2])
                if "/" in part: res = int(part[0]) // int(part[2])
            del arr[openb:closeb+1]
            arr.insert(openb, res)
        while "+" in arr or "-" in arr or "*" in arr or "/" in arr:
            indm, indd, inda, inds = 1000, 1000, 1000, 1000
            if "*" in arr or "/" in arr:
                if "*" in arr: indm = arr.index("*")
                if "/" in arr: indd = arr.index("/")
                indop = min(indm, indd)
            elif "+" in arr or "-" in arr:
                if "+" in arr: inda = arr.index("+")
                if "-" in arr: inds = arr.index("-")
                indop = min(inda, inds)
            a = float(arr[indop-1])
            b = float(arr[indop+1])
            if arr[indop] == "+":
                res = a + b
            elif arr[indop] == "-":
                res = a - b
            elif arr[indop] == "*":
                res = a * b
            elif arr[indop] == "/":
                res = a // b
            print(f"indop = {indop}")
            print(res)
            del arr[indop-1:indop+2]
            print(arr)
            arr.insert(indop-1, res)
            print(arr)
        arr = [str(el) for el in arr]
        return float("".join(arr))