def isAMatch(grid, position):
    x, y = position
    
    if grid[x][y] == 'A':
        # M.M
        # .A.
        # S.S
        if (grid[x-1][y-1] == 'M' and grid[x-1][y+1] == 'M' and grid[x+1][y-1] == 'S' and grid[x+1][y+1] == 'S'):
            return True
        
        # M.S
        # .A.
        # M.S
        if (grid[x-1][y-1] == 'M' and grid[x-1][y+1] == 'S' and grid[x+1][y-1] == 'M' and grid[x+1][y+1] == 'S'):
            return True
        
        # S.M
        # .A.
        # S.M
        if (grid[x-1][y-1] == 'S' and grid[x-1][y+1] == 'M' and grid[x+1][y-1] == 'S' and grid[x+1][y+1] == 'M'):
            return True
        
        # S.S
        # .A.
        # M.M
        if (grid[x-1][y-1] == 'S' and grid[x-1][y+1] == 'S' and grid[x+1][y-1] == 'M' and grid[x+1][y+1] == 'M'):
            return True
    return False

with open('day04/input.txt') as f:
    map = [line.strip() for line in f.readlines()]
    print(map)

    count = 0
    for x in range(1, len(map)-1):
        for y in range(1, len(map[x])-1):
            count += isAMatch(map, (x, y))
    
    print(count)