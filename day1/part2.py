with open('input.txt') as f:
    list1, list2 = [], []

    lines = f.readlines()
    
    for line in lines:
        list1.append(int(line.split()[0]))
        list2.append(int(line.split()[1].rstrip('\n')))
    
    score = 0
    for i in range(len(list1)):
        score += list2.count(list1[i]) * list1[i]
    
    print(score)