import random

'''
import random

n = 20

dataset = [[0 for j in range(n)] for i in range(n)]

dataset[0][0] = 100

for i in range(1, n):
    dataset[i][0] = dataset[i-1][0] + random.randint(-2, 5)

for j in range(1, n):
    dataset[0][j] = dataset[0][j-1] + random.randint(-2, 5)

for i in range(1, n):
    for j in range(1, n):
        dataset[i][j] = (dataset[i-1][j-1]+dataset[i-1][j]+dataset[i][j-1])//3 + random.randint(-1,1)


with open("KNN.txt", "w") as f:
    for i in range(n):
        for j in range(n):
            f.write(str(dataset[i][j])+' ')
        f.write('\n')
        
        
'''

with open("KNN.txt", "r") as f:
    dataset = []
    for line in f:
        dataset += [list(map(int, line.split()))]
    n = len(dataset)


train = [["-" for j in range(n)] for i in range(n)]

for i in range(n**2//5):
    flag = False
    while not flag:
        x = random.randint(0, n-1)
        y = random.randint(0, n-1)
        if train[x][y] == '-':
            train[x][y] = dataset[x][y]
            flag = True

test = [[0 for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        if train[i][j] != '-':
            test[i][j] = train[i][j]
        else:
            nns = []
            k = 3
            k1 = k
            t = 1
            while k1 > 0:
                for x in range(-t, t+1):
                    for y in (-t, t):
                        if i+x >= 0 and i+x <= n-1 and j+y >= 0 and j+y <= n-1:
                            if train[i+x][j+y] != '-':
                                nns += [train[i+x][j+y]]
                                k1 -= 1

                for y in range(-t+1, t):
                    for x in (-t, t):
                        if i+x >= 0 and i+x <= n-1 and j+y >= 0 and j+y <= n-1:
                            if train[i+x][j+y] != '-':
                                nns += [train[i+x][j+y]]
                                k1 -= 1
                t += 1

            while len(nns) > k:
                nns.pop()

            test[i][j] = sum(nns)//k

with open("KNN_test.txt", "w") as f:
    for i in range(n):
        for j in range(n):
            f.write(str(test[i][j]) + ' ')
        f.write('\n')

errors = [[dataset[i][j]-test[i][j] for j in range(n)] for i in range(n) ]

with open("KNN_errors.txt", "w") as f:
    for i in range(n):
        for j in range(n):
            f.write(str(errors[i][j]) + ' ')
        f.write('\n')




















