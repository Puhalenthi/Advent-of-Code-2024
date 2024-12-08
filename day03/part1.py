import regex as re

with open('input.txt') as f:
    lines = f.readlines()
    result = 0
    for line in lines:
        resultReg = re.findall(r'mul\(([0-9]+),([0-9]+)\)', line)
        for x, y in resultReg:
            result += int(x) * int(y)
    
    print(result)