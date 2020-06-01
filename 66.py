import io
import math
import random
from tkinter import Tk, Canvas, Frame, BOTH, filedialog

from PIL import Image

class Example(Frame):

    canvas = Canvas

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        global flag, canvas
        self.parent.title("Colours")
        self.pack(fill=BOTH, expand=1)
        canvas.self = Canvas(self, bg='black')

    def draw(self):
        global canvas, a, mouseX, mouseY
        canvas.self.delete('all')
        canvas.self.create_rectangle(0, 0, 500, 500, fill='black')
        for i in range(len(a)):
            eDist = math.sqrt((mouseX-a[i][0])**2+(mouseY-a[i][1])**2)
            eSize = round(eDist/2)
            eColor = round(eDist+50)
            if eColor > 255:
                eColor = 255
            de = "%02x" % (eColor)
            ge = '#'
            cx = a[i][0]
            cy = a[i][1]
            color = ge + de + de + de
            canvas.self.create_oval(cx+eSize/2, cy+eSize/2, cx-eSize/2, cy-eSize/2, fill=color)
        canvas.self.pack(fill=BOTH, expand=1)


def s(event):
    global canvas
    canvas.self.update()
    canvas.self.postscript(colormode='color')
    ps = canvas.self.postscript(colormode='color')
    hen = filedialog.asksaveasfilename(defaultextension='')
    im = Image.open(io.BytesIO(ps.encode('utf-8')))
    im.save(hen + '.png')

def b1(event):
    global mouseX, mouseY
    mouseX = event.x
    mouseY = event.y
    ex.draw()

a = list()
for i in range(500):
    b = []
    for j in range(2):
        b.append(random.randint(10, 490))
    a.append(b)
mouseX, mouseY = 0, 0
canvas = Canvas
root = Tk()
root.geometry("500x500+300+300")
flag = 1
root.bind('<s>', s)
root.bind('<Button-1>', b1)
ex = Example(root)
ex.draw()
root.mainloop()