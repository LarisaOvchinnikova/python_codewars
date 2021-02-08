# https://www.codewars.com/kata/57e90bcc97a0592126000064
def sea_sick(sea):
    count = 0
    for i in range(len(sea)-1):
        if sea[i] == "~" and sea[i+1] == '_' or sea[i] == "_" and sea[i+1] == '~':
            count+=1
    return "Throw Up" if count > len(sea) / 5 else "No Problem"