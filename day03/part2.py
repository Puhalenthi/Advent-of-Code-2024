import regex as re

with open('day03/input.txt') as f:
    lines = f.readlines()
    result = 0

    line = ''.join(lines)
    
    while re.search(r'don\'t.*?do\(', line):
        line = re.sub(r'don\'t.*?do\(', '', line)
    
    index = line.index("don't()")
    line = line[:index]
    print(line)



    resultReg = re.findall(r'mul\(([0-9]+),([0-9]+)\)', line)
    for x, y in resultReg:
        result += int(x) * int(y)
    
    print(result)