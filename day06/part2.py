def runSimulation(map, startingCoords):
    visited = set()
    direction = 'N'
    x, y = startingCoords
    # run simulation until player exits the map
    count = 0
    while True:
        visited.add((x, y, direction))
        count += 1
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
            return False
        if ((x, y, direction) in visited):
            return True


with open('day06/input.txt') as f:
    map = [line.strip() for line in f.readlines()]
    x, y = 0, 0
    # locate ^
    for i, row in enumerate(map):
        if '^' in row:
            x, y = i, row.index('^')
            break
    
    countSimulations = 0
    count = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            newMap = map.copy()
            newMap[i] = newMap[i][:j] + '#' + newMap[i][j+1:]
            print(x, y)
            countSimulations += int(runSimulation(newMap, (x, y)))
            count += 1
            print(count/(len(map)*len(map[i])))
            #print(newMap)
    
    print(countSimulations)