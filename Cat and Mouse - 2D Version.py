# https://www.codewars.com/kata/57f8842367c96a89dc00018e
def cat_mouse(map, moves):
    map = map.split('\n')
    cat_x, cat_y, mouse_x, mouse_y = '', '', '', ''
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "C":
                cat_x = i
                cat_y = j
            if map[i][j] == "m":
                mouse_x = i
                mouse_y = j
    if cat_x == '' or mouse_x == '': return 'boring without two animals'
    return 'Escaped!' if abs(cat_x - mouse_x) + abs(cat_y - mouse_y) > moves  else 'Caught!'