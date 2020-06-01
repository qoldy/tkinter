from PIL import Image


def make_bezier(xys):
    n = len(xys)
    combinations = pascal_row(n-1)
    def bezier(ts):
        result = []
        for t in ts:
            tpowers = (t**i for i in range(n))
            upowers = reversed([(1-t)**i for i in range(n)])
            coefs = [c*a*b for c, a, b in zip(combinations, tpowers, upowers)]
            result.append(
                tuple(sum([coef*p for coef, p in zip(coefs, ps)]) for ps in zip(*xys)))
        return result
    return bezier

def pascal_row(n):
    # This returns the nth row of Pascal's Triangle
    result = [1]
    x, numerator = 1, n
    for denominator in range(1, n//2+1):
        # print(numerator,denominator,x)
        x *= numerator
        x /= denominator
        result.append(x)
        numerator -= 1
    if n&1 == 0:
        # n is even
        result.extend(reversed(result[:-1]))
    else:
        result.extend(reversed(result))
    return result

import io
import math
from tkinter import Tk, Canvas, Frame, BOTH, filedialog


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
        canvas.self.create_rectangle(0, 0, 800, 800, fill="black")

    def draw(self):
        global mouseX, mouseY
        global num
        width, height = 800, 800

        maxX = mouseX/width*300-150
        maxY = mouseY/height*300-150

        for i in range(0, 360, 2):
            angle = math.sin(i + num)
            x = math.sin(math.radians(i)) * (maxX + angle * 30)
            y = math.cos(math.radians(i)) * (maxX + angle * 30)
            x2 = math.sin(math.radians(i + num * 50)) * (maxY + angle * 60)
            y2 = math.cos(math.radians(i + num * 50)) * (maxY + angle * 60)

            pathR = round(50 + angle + 125 * math.fabs(math.sin(math.pi + num * 3)))
            pathG = round(50 + angle + 125 * math.fabs(math.sin(math.pi*2 + num * 9)))
            pathB = round(50 + angle + 125 * math.fabs(math.sin(math.pi/2 + num * 3)))
            color = '#%02x%02x%02x' % (pathR, pathG, pathB)

            xys = [(x+400, y+400), (x+x+400, y+y+400), (x+x2+400, y+y2+400), (x+x2+400, y+y2+400)]
            ts = [t / 100.0 for t in range(101)]
            bezier = make_bezier(xys)
            points = bezier(ts)
            for j in range(len(points) - 1):
                 canvas.self.create_line(points[j][0], points[j][1], points[j + 1][0], points[j + 1][1], fill=color)
        canvas.self.pack(fill=BOTH, expand=1)
        num += 0.01


def s(event):
    global canvas
    canvas.self.update()
    canvas.self.postscript(colormode='color')
    ps = canvas.self.postscript(colormode='color')
    hen = filedialog.asksaveasfilename(defaultextension='')
    im = Image.open(io.BytesIO(ps.encode('utf-8')))
    im.save(hen + '.png')


def b1(event):
    global mouseX
    global mouseY
    mouseX = event.x
    mouseY = event.y
    ex.draw()


mouseX, mouseY, num = 250, 250, 2

canvas = Canvas
root = Tk()
root.geometry("800x800+300+300")
flag = 1
root.bind('<s>', s)
root.bind('<Button-1>', b1)
ex = Example(root)
ex.draw()
root.mainloop()
