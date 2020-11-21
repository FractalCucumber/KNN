import random

n = 2000

with open("datasetKNN.txt", "w") as f:

    for _ in range(n):
        x = round(random.uniform(1, 100), 3)
        y = round(random.uniform(1, 100), 3)

        r = (x-50)**2 + (y-50)**2
        R1 = 25**2
        R2 = 50**2
        if r >= R1 and r <= R2:
            class_xy = "class1"
        elif r < R1:
            class_xy = "class2"
        else:
            class_xy = "class3"

        f.write(str(x)+" "+str(y)+" "+class_xy+"\n")



'''
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

'''