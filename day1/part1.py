with open('input.txt') as f:
    list1, list2 = [], []

    lines = f.readlines()
    
    for line in lines:
        list1.append(int(line.split()[0]))
        list2.append(int(line.split()[1].rstrip('\n')))
    
    list1, list2 = sorted(list1), sorted(list2)
    sum = 0
    for i in range(len(list1)):
        sum += abs(list1[i] - list2[i])
    
    print(sum)