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


    def drawLine(self, ncx, ncy, counter1):

        x1 = ncx - math.sin(counter1)*100
        y1 = ncy - math.cos(counter1)*100
        x2 = ncx + math.sin(counter1)*100
        y2 = ncy + math.cos(counter1)*100
        canvas.self.create_line(x1, y1, x2, y2, fill='white')

    def draw(self):
        global cx, cy, cRadius, counter1
        counter = 0
        loopcount = 1
        canvas.self.create_rectangle(0, 0, 800, 800, fill="black")
        while True:
            nx = math.sin(counter1)*cRadius + cx
            ny = math.cos(counter1)*cRadius + cy
            x1 = nx - math.sin(counter)*150
            x2 = nx + math.sin(counter)*150
            y1 = ny - math.cos(counter)*150
            y2 = ny + math.cos(counter)*150

            self.drawLine(x2, y2, counter1)
            self.drawLine(x1, y1, counter1)
            counter += 0.1
            if counter > 2*math.pi:
                counter = 0
            counter1 += 0.01
            cRadius+=counter/20
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


counter1 = 0
cx = 400
cy = 350
cRadius = 20
canvas = Canvas
root = Tk()
root.geometry("800x800")
flag = 1
root.bind('<s>', s)
ex = Example(root)
ex.draw()
root.mainloop()