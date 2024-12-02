with open("input.txt") as f:
    lines = f.read().splitlines()
    safe = 0
    for line in lines:
        levels = line.split()
        levels = [int(x) for x in levels]

        if all(levels[i] < levels[i + 1] for i in range(len(levels) - 1)) or all(levels[i] > levels[i + 1] for i in range(len(levels) - 1)):
            if all((abs(levels[i] - levels[i + 1]) >= 1) and (abs(levels[i] - levels[i + 1]) <= 3) for i in range(len(levels) - 1)):
                safe += 1
                print(line)
    print(safe)