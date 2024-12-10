from itertools import product

def evaluateEquation(equation):
    numbers = equation.split()
    total = int(numbers[0])
    for i in range(1, len(numbers), 2):
        if numbers[i] == '+':
            total += int(numbers[i+1])
        elif numbers[i] == '*':
            total *= int(numbers[i+1])
        elif numbers[i] == '||':
            total = int(str(total) + str(numbers[i+1]))
    return total

def checkIfPossible(total, equation):
    numbers = equation.split()
    operators = ['+', '*', '||']
    for ops in product(operators, repeat=len(numbers)-1):
        expr = ''.join(f"{num} {op} " for num, op in zip(numbers, ops + ('',)))
        if evaluateEquation(expr) == total:
            return True
    
    return False

with open('day07/input.txt') as file:
    lines = file.read().splitlines()

    finalTotal = 0
    for line in lines:
        total = int(line[:line.index(': ')])
        equation = line[line.index(': ')+2:]

        if checkIfPossible(total, equation):
            finalTotal += total
    
    print(finalTotal)