def findMatchesCount(grid, position): # VERY dirty code
    x, y = position
    count = 0
    

    if grid[x][y] == 'X':
        try:
            if not (y <= len(grid[x])-3): # check if y does not exceed the grid
                pass
            elif (grid[x][y+1] == 'M' and grid[x][y+2] == 'A' and grid[x][y+3] == 'S'):  # Right
                count += 1
                print(x, y)
        except IndexError:
            pass
        try:
            if not (y >= 3): # check if y does not exceed the grid
                pass
            elif (grid[x][y-1] == 'M' and grid[x][y-2] == 'A' and grid[x][y-3] == 'S'): # Left
                count += 1
                print(x, y)
        except IndexError:
            pass
        try:
            if not (x <= len(grid)-3): # check if x does not exceed the grid
                pass
            elif (grid[x+1][y] == 'M' and grid[x+2][y] == 'A' and grid[x+3][y] == 'S'): # Down
                count += 1
                print(x, y)
        except IndexError:
            pass
        try:
            if not (x >= 3): # check if x does not exceed the grid
                pass
            elif (grid[x-1][y] == 'M' and grid[x-2][y] == 'A' and grid[x-3][y] == 'S'): # Up
                count += 1
                print(x, y)
        except IndexError:
            pass
        try:
            if not (x <= len(grid)-3 and y <= len(grid[x])-3):
                pass
            elif (grid[x+1][y+1] == 'M' and grid[x+2][y+2] == 'A' and grid[x+3][y+3] == 'S'): # Down Right
                count += 1
                print(x, y)
        except IndexError:
            pass
        try:
            if not (x <= len(grid)-3 and y >= 3):
                pass
            elif (grid[x+1][y-1] == 'M' and grid[x+2][y-2] == 'A' and grid[x+3][y-3] == 'S'): # Down Left
                count += 1
                print(x, y)
        except IndexError:
            pass
        try:
            if not (x >= 3 and y <= len(grid[x])-3):
                pass
            elif (grid[x-1][y+1] == 'M' and grid[x-2][y+2] == 'A' and grid[x-3][y+3] == 'S'): # Up Right
                count += 1
                print(x, y)
        except IndexError:
            pass
        try:
            if not (x >= 3 and y >= 3):
                pass
            elif (grid[x-1][y-1] == 'M' and grid[x-2][y-2] == 'A' and grid[x-3][y-3] == 'S'): # Up Left
                count += 1
                print(x, y)
        except IndexError:
            pass
    return count


with open('day04/input.txt') as f:
    map = [line.strip() for line in f.readlines()]
    print(map)

    count = 0
    for x in range(len(map)):
        for y in range(len(map[x])):
            count += findMatchesCount(map, (x, y))
    
    print(count)