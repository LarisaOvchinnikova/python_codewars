https://www.codewars.com/kata/59d0ee709f0cbcf65400003b
def by_state(s):
    s = s.strip()
    states = {
        'AZ': 'Arizona',
        'CA': 'California',
        'ID': 'Idaho',
        'IN': 'Indiana',
        'MA': 'Massachusetts',
        'OK': 'Oklahoma',
        'PA': 'Pennsylvania',
        'VA': 'Virginia'
    }
    arr = s.replace(',', '').split('\n')
    arr = sorted(arr, key=lambda el:(el[-2:],el))
    friends = []
    for key in states:
        state = []
        for el in arr:
            if el[-2:] == key:
                state.append(states[el[-2:]])
                state.append('..... ' + el[:-2]+states[el[-2:]])
        state = [el for i,el in enumerate(state) if i == state.index(el) ]
        state = "\r\n".join(state)
        if state != '':
            friends.append(state)
    friends = [el for el in friends if el != []]
    return "\r\n ".join(friends)