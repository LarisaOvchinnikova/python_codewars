# https://www.codewars.com/kata/576757b1df89ecf5bd00073b


def tower_builder(n):
    return [("*" * i).center(n * 2 - 1) for i in range(1, n * 2, 2)]