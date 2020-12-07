#https://www.codewars.com/kata/57e3f79c9cb119374600046b/train/python
def hello(name=""):
    if name:
        return "Hello, " + name.title() + "!"
    else:
        return "Hello, World!"