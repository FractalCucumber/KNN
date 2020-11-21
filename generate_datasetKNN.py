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