https://www.codewars.com/kata/56c22c5ae8b139416c00175d
def match(candidate, job):
    return candidate['min_salary'] * 0.9 <= job['max_salary']