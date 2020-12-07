https://www.codewars.com/kata/57ae18c6e298a7a6d5000c7a
def replace_all(obj, find, replace):
    return [replace if el == find else el for el in obj] if type(obj)==list else  replace.join(obj.split(find))