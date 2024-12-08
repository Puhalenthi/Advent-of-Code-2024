import math
import itertools

def processRules(rules):
    dictionary = {}
    for rule in rules:
        k, v = rule.split('|')
        if int(k) in dictionary.keys():
            dictionary[int(k)].append(int(v))
        else:
            dictionary[int(k)] = [int(v)]
    return dictionary

def processUpdates(updates):
    lst = []
    for update in updates:
        temp = []
        for i in update.split(','):
            temp += [int(i)]
        lst.append(temp)
    return lst

def checkIfValid(rules, update):
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            if update[j] in rules.keys():
                if update[i] in rules[update[j]]:
                    return False
    return True

def testPossibleCombinations(rules, update):
    combinations = list(itertools.permutations(update, len(update)))
    for i in combinations:
        if checkIfValid(rules, i):
            return i


with open('day05/input.txt') as f:
    data = f.read().strip().split('\n')
    rules, updates = data[0:data.index('')], data[data.index('')+1:]

    rules = processRules(rules)
    updates = processUpdates(updates)

    validUpdates = []
    for update in updates:
        if not checkIfValid(rules, update):
            validUpdates.append(testPossibleCombinations(rules, update))
    
    total = 0
    for i in validUpdates:
        total += i[math.floor(len(i)/2)]

    print(validUpdates)
    
    print(total)