def calBudget():
    vals = []
    vals = input()
    vals = vals.split()
    N = int(vals[0])
    K = int(vals[1])
    P = int(vals[2])
    sumValues = []
    for i in range(N):
        beautyValues = []
        add = 0
        for k in range(K):
            beautyValues = input()
            beautyValues = beautyValues.split()
            beautyValues = [int(j) for j in beautyValues]
            l = 0
            listLength = len(beautyValues)
            while l < listLength:
                if beautyValues[l] <= beautyValues[l+1]:
                    add = add + beautyValues[l]
                l += 1
            sumValues.append(add)
    return sumValues

ls = []
T = int(input())
for i in range(T):
    a = calBudget()
    a = int(a)
    ls.append(a)
for i in range(T):
    print('case #%d: %d' % (i+1,ls[i]))