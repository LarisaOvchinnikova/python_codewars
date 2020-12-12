# https://www.codewars.com/kata/5f5802bf4c2cc4001a6f859e
def grid_index(grid, indexes):
    gr = []
    for el in grid:
        gr.extend(el)
    return "".join([gr[el-1] for el in indexes])