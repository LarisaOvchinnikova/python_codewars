# https://www.codewars.com/kata/58f6e7e455d7597dcc000045
def get_password(grid,directions):
    for i, row in enumerate(grid):
        if 'x' in row:
            start_x = i
            start_y = row.index('x')
    password = ''
    for el in directions:
        if el.startswith('right'):
            start_y += 1
        if el.startswith('left'):
            start_y -= 1
        if el.startswith('down'):
            start_x += 1
        if el.startswith('up'):
            start_x -= 1
        if el[-1] == "T":
            password += grid[start_x][start_y]
    return password