https://www.codewars.com/kata/5c511d8877c0070e2c195faf
def validate(username, password):
    n = math.ceil(min(len(username), len(password)) / 2)
    for i in range(len(password)-n+1):
        if password[i: i+n] in username:
            return False
    else:
        return True