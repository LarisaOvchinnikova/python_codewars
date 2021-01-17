# https://www.codewars.com/kata/5d076515e102162ac0dc514e
def baby_shark_lyrics():
    a = ['Baby shark','Mommy shark','Daddy shark','Grandma shark','Grandpa shark','Let\'s go hunt']
    s = ''
    for i in range(len(a)):
        s += (a[i] + ', ' + 'doo ' * 5 + 'doo\n') * 3 + a[i] + '!\n'
    return s + 'Run away,…'