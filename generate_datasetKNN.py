import random

n = 5000

with open("datasetKNN.txt", "w") as f:

    for _ in range(n):
        x = round(random.uniform(1, 100), 3)
        y = round(random.uniform(1, 100), 3)

        r = (x-50)**2 + (y-50)**2
        R1 = 25**2
        R2 = 50**2
        if r < R1:
            class_xy = "class1"
        elif r >= R1 and r <= R2:
            class_xy = "class2"
        else:
            class_xy = "class3"

        f.write(str(x)+" "+str(y)+" "+class_xy+"\n")

with open("datasetKNN2.txt", "w") as f:

    for _ in range(n):
        x = round(random.uniform(1, 100), 3)
        y = round(random.uniform(1, 100), 3)

        if x<=50 and y<=50:
            class_xy = "class1"
        elif x>50 and y<=50:
            class_xy = "class2"
        elif x<=50 and y>50:
            class_xy = "class3"
        else:
            class_xy = "class4"

        f.write(str(x)+" "+str(y)+" "+class_xy+"\n")


with open("datasetKNN3.txt", "w") as f:
    for _ in range(n):
        R1 = 20**2
        R2 = 10**2
        R3 = 25**2

        x = round(random.uniform(1, 100), 3)
        y = round(random.uniform(1, 100), 3)

        r1 = (x - 25) ** 2 + (y - 40) ** 2
        r2 = (x - 70) ** 2 + (y - 60) ** 2
        r3 = (x - 60) ** 2 + (y - 20) ** 2


        if (r1 >= 0 and r1 <= R1):
            class_xy = "class1"
        elif (r2 >= R2 and r2 <= R3):
            class_xy = "class2"
        elif (r3 >= 0 and r3 <= R2):
            class_xy = "class3"
        elif y >= -x+50:
            class_xy = "class4"
        else:
            class_xy = "class5"




        f.write(str(x) + " " + str(y) + " " + class_xy + "\n")