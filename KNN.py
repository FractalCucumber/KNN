import random
import tkinter

input_file = "datasetKNN3.txt"

with open(input_file, "r") as f:
    dataset = dict()

    for line in f:
        line = line.split()
        xy = tuple(map(float, line[:-1:]))
        class_xy = line[-1]

        dataset[xy] = class_xy

n = len(dataset)
k = 3

with open("KNN_train.txt", "w") as f:
    train_xy = random.sample(dataset.keys(), n//5)
    for i in train_xy:
        f.write(" ".join(map(str, i))+" "+dataset[i]+"\n")

test = dict()


nns = dict()

for xy in dataset.keys():
    if not xy in train_xy:
        x = xy[0]
        y = xy[1]

        nns[xy] = list(map(lambda t: t[0], sorted([(i, (i[0]-x)**2 + (i[1]-y)**2) for i in train_xy], key=lambda j: j[1])[:k:]))

        c = dict()
        for i in nns[xy]:
            if dataset[i] not in c:
                c[dataset[i]] = 1
            else:
                c[dataset[i]] += 1

        p = k*random.random()
        pc = 0

        for i in c:
            pc += c[i]
            if p <= pc:
                class_xy = i
                break

        test[xy] = class_xy

with open("KNN_test.txt", "w") as f:
    for i in test:
        f.write(" ".join(map(str, i))+" "+test[i]+"\n")


error = 0
for i in test.keys():
    if test[i] != dataset[i]:
        error += 1






window = tkinter.Tk()

canvas = tkinter.Canvas(window, width=700, height=700, bg="white", cursor="pencil")


def plot(s, sign, dx, dy):
    colors = {"class1": "khaki1", "class2": "blue", "class3": "aquamarine4", "class4": "MediumPurple1", "class5": "seashell3"}
    with open(s, "r") as f:
        dataset = dict()

        for line in f:
            line = line.split()
            xy = tuple(map(float, line[:-1:]))
            class_xy = line[-1]

            dataset[xy] = class_xy

    for i in dataset:
        x = i[0]*3 + dx
        y = i[1]*3 + dy
        color = colors[dataset[i]]
        canvas.create_oval(x, y, x+3, y+3, outline=color, fill=color)

    canvas.create_text(dx+150, dy+320, text=sign)

plot(input_file, "dataset", 0, 200)
plot("KNN_train.txt", "train", 350, 0)
plot("KNN_test.txt", "test", 350, 350)

canvas.create_text(300, 680, text="Percentage of errors: "+str(100*error/(n-n//5))+"%")

canvas.pack()
window.mainloop()

