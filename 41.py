import io
import math
from tkinter import Tk, Canvas, Frame, BOTH, filedialog

from PIL import Image

class Example(Frame):


    canvas = Canvas
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()


    def initUI(self):
        global flag
        self.parent.title("Colours")
        self.pack(fill=BOTH, expand=1)
        canvas.self = Canvas(self, bg='black')

    def draw(self):
        global cx, cy, cRadius
        counter, counter1 = 0, 0
        loopcount = 0
        canvas.self.create_rectangle(0, 0, 500, 500, fill="white")
        while True:
            nx = math.sin(counter1)*cRadius + cx
            ny = math.cos(counter1)*cRadius + cy
            x1 = nx - math.sin(counter)*200
            x2 = nx + math.sin(counter)*200
            y1 = ny - math.cos(counter)*200
            y2 = ny + math.cos(counter)*200
            canvas.self.create_line(x1, y1, x2, y2, fill='black')
            counter += 0.1
            if counter > 2*math.pi:
                counter = 0
            counter1 += 0.01
            if counter1 > 2*math.pi:
                break
        canvas.self.pack(fill=BOTH, expand=1)


def s(event):
    global canvas
    canvas.self.update()
    canvas.self.postscript(colormode='color')
    ps = canvas.self.postscript(colormode='color')
    hen = filedialog.asksaveasfilename(defaultextension='')
    im = Image.open(io.BytesIO(ps.encode('utf-8')))
    im.save(hen + '.png')



cx = 250
cy = 250
cRadius = 200
canvas = Canvas
root = Tk()
root.geometry("500x500+300+300")
flag = 1
root.bind('<s>', s)
ex = Example(root)
ex.draw()
root.mainloop()