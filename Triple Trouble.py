https://www.codewars.com/kata/5704aea738428f4d30000914
def triple_trouble(one, two, three):
    return "".join([one[i]+two[i]+three[i] for i in range(len(one))])