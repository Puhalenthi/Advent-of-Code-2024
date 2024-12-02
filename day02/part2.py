def checkIfSafe(levels):
    if all(levels[i] < levels[i + 1] for i in range(len(levels) - 1)) or all(levels[i] > levels[i + 1] for i in range(len(levels) - 1)):
        if all((abs(levels[i] - levels[i + 1]) >= 1) and (abs(levels[i] - levels[i + 1]) <= 3) for i in range(len(levels) - 1)):
            return True
    return False

def checkMultSafe(levels):
    for i in range(len(levels)):
        if checkIfSafe(levels[:i] + levels[i + 1:]):
            return True
    return False


with open('input.txt') as f:
    lines = f.read().splitlines()
    safe = 0
    for line in lines:
        levels = line.split()
        levels = [int(x) for x in levels]
        if checkMultSafe(levels):
            safe += 1
    print(safe)