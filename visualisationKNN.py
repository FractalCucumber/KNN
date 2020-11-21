import tkinter

window = tkinter.Tk()

canvas = tkinter.Canvas(window, width=700, height=700, bg="white", cursor="pencil")


def grafic(s, sign, dx, dy):
    colors = {"class1": "blue", "class2": "green", "class3": "purple"}
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
        canvas.create_oval(x, y, x+5, y+5, outline=color, fill=color)

    canvas.create_text(dx+150, dy+320, text=sign)

grafic("datasetKNN.txt", "dataset", 0, 200)
grafic("KNN_train.txt", "train", 350, 0)
grafic("KNN_test.txt", "test", 350, 350)


canvas.pack()
window.mainloop()