def calBudget():
    vals = []
    vals = input()
    vals = vals.split()
    N = int(vals[0])
    B = int(vals[1])
    cost = []
    cost = input()
    cost = cost.split()
    cost = [int(j) for j in cost]
    cost.sort()
    Bsum = 0    
    count = 0
    for j in cost:
        if Bsum <= B:
            Bsum = Bsum + j
            count += 1
            if Bsum > B:
                Bsum = Bsum - j
                count -= 1
    return count

ls = []
T = int(input())
for i in range(T):
    a = calBudget()
    a = int(a)
    ls.append(a)
for i in range(T):
    print('case #%d: %d' % (i+1,ls[i]))