# https://www.codewars.com/kata/5c784110bfe2ef660cb90369
def ranking(people):
    if people == [] : return []
    people = sorted(people, key=lambda el:el["points"],reverse=True)
    people[0]["position"] = 1
    pos = 1
    for i in range(1,len(people)):
        if people[i]["points"] == people[i-1]["points"]:
            people[i]["position"]= people[i-1]["position"]
            pos+=1
        else:
            pos+=1
            people[i]["position"]= pos
    people = sorted(people, key=lambda el:(el["position"],el["name"]))
    return people