import math
import random
from tkinter import Tk, Canvas, Frame, BOTH

import noise as noise


class FunnyEllipse:
    x, y, size, color, noise = 0, 0, 0, 'white', False

    def __init__(self):
        self.size = random.randint(50, 150)

    def render(self):
        global canvas
        if self.noise:
            nx = random.randint(10, 40)*10
            ny = random.randint(10, 40)*10
            self.x, self.y = nx, ny
            canvas.self.create_oval(nx, ny, nx+self.size, ny + self.size, outline=self.color, fill='')
        else:
            canvas.self.create_oval(self.x, self.y, self.x + self.size, self.y + self.size, outline=self.color, fill='')
        canvas.self.pack(fill=BOTH, expand=1)

    def isLine(self, box):
        result = False
        if math.sqrt((self.x - box.x)**2 + (self.y - box.y)**2) < 150:
            self.drawLine(box)
            result = True
            self.noise = True
            box.noise = True
            self.color = 'white'
            box.color = 'white'
        else:
            self.noise = False
            box.noise = False
        return result

    def drawLine(self, box):
        global canvas
        canvas.self.create_line(self.x+self.size/2, self.y+self.size/2, box.x+box.size/2, box.y+box.size/2, fill='white')
        canvas.self.create_oval(self.x+self.size/2+5, self.y+self.size/2+5, self.x+self.size/2-5, self.y+self.size/2-5, fill='white')
        canvas.self.create_oval(box.x+box.size/2+5, box.y+box.size/2+5, box.x+box.size/2 - 5, box.y+box.size/2 - 5, fill='white')
        canvas.self.pack(fill=BOTH, expand=1)


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        global canvas
        self.parent.title("Colours")
        self.pack(fill=BOTH, expand=1)
        canvas.self = Canvas(self)
        canvas.self.create_rectangle(0, 0, 500, 500, fill='black')

    def draw(self):
        global obj_1, obj_2, counter
        obj_1.x = math.sin(counter)*150 + 250
        obj_2.x = math.cos(counter)*150 + 250
        obj_2.y = math.sin(counter+0.1)*150 + 250
        obj_1.y = math.cos(counter-0.1)*150 + 250
        obj_1.color = 'red'
        obj_2.color = 'red'
        obj_1.render()
        obj_2.render()
        counter += 0.1


def b1(event):
    global canvas, ex, start, obj_1, obj_2
    if obj_1.noise:
        canvas.self.delete('all')
        canvas.self.create_rectangle(0, 0, 500, 500, fill='black')
        obj_1.render()
        obj_2.render()
        if obj_1.isLine(obj_2):
            obj_1.drawLine(obj_2)
    else:
        canvas.self.delete('all')
        canvas.self.create_rectangle(0, 0, 500, 500, fill='black')
        ex.draw()
        if obj_1.isLine(obj_2):
            obj_1.drawLine(obj_2)


start = False
canvas = Canvas
obj_1, obj_2 = FunnyEllipse(), FunnyEllipse()
counter = 0
root = Tk()
root.geometry("500x500")
root.bind('<Button-1>', b1)
ex = Example(root)
obj_1.render()
obj_2.render()
root.mainloop()
