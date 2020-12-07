https://www.codewars.com/kata/53573877d5493b4d6e00050c/train/python
def capital(capitals):
    res = []
    for el in capitals:
        if 'state' in el:
            res.append(f"The capital of {el['state']} is {el['capital']}")
        else:
            res.append(f"The capital of {el['country']} is {el['capital']}")
    return res
print()

ef capital(capitals):
    return [f"The capital of {el['state']} is {el['capital']}" if "state" in el else f"The capital of {el['country']} is {el['capital']}"  for el in capitals]