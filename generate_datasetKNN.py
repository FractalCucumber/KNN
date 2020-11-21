import random

n = 20

dataset = [[0 for j in range(n)] for i in range(n)]
dataset[0][0] = 100

for i in range(1, n):
    dataset[i][0] = dataset[i - 1][0] + random.randint(-2, 5)

for j in range(1, n):
    dataset[0][j] = dataset[0][j - 1] + random.randint(-2, 5)

for i in range(1, n):
    for j in range(1, n):
        dataset[i][j] = (dataset[i - 1][j - 1] + dataset[i - 1][j] + dataset[i][j - 1]) // 3 + random.randint(-1, 1)

with open("datasetKNN.txt", "w") as f:
    for i in range(n):
        for j in range(n):
            f.write(str(dataset[i][j]) + ' ')
        f.write('\n')

