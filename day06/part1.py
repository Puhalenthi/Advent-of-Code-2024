with open('input.txt') as f:
    map = [line.strip() for line in f.readlines()]
    # locate ^
    for i, row in enumerate(map):
        if '^' in row:
            x, y = i, row.index('^')
            break
    
    visited = set()
    direction = 'N'
    # run simulation until player exits the map
    while True:
        visited.add((x, y))
        if direction == 'N':
            try:
                if map[x-1][y] == '#':
                    direction = 'E'
                else:
                    x, y = x-1, y
            except IndexError:
                x, y = x-1, y
        elif direction == 'E':
            try:
                if map[x][y+1] == '#':
                    direction = 'S'
                else:
                    x, y = x, y+1
            except IndexError:
                x, y = x, y+1
        elif direction == 'S':
            try:
                if map[x+1][y] == '#':
                    direction = 'W'
                else:
                    x, y = x+1, y
            except IndexError:
                x, y = x+1, y
        elif direction == 'W':
            try:
                if map[x][y-1] == '#':
                    direction = 'N'
                else:
                    x, y = x, y-1
            except IndexError:
                x, y = x, y-1
        
        if (x < 0 or x >= len(map)) or (y < 0 or y >= len(map[0])):
            break
    print(len(visited))