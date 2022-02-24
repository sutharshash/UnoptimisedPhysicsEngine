import tkinter

import numpy
from PIL import Image
import math
from tkinter import colorchooser

RGB = colorchooser.askcolor(title ="Choose color")
print(RGB)
print(RGB[0][0])
def Sphere(R, Fill = False):
    Viewport = numpy.zeros((1000, 1000, 3), dtype=numpy.uint8)
    Trash = 0
    if Fill == True:
        Viewport = numpy.zeros((1000, 1000, 3), dtype=numpy.uint8)
        Trash = 0
        while Trash <= 2 * math.pi * R:
            Trash += 0.1
            X = R * math.cos(Trash)
            Y = R * math.sin(Trash)
            Viewport[(500-int(X)):(500 + int(X)), int(Y)+500, 0] = RGB[0][0]
            Viewport[(500-int(X)):(500 + int(X)), int(Y)+500, 1] = RGB[0][1]
            Viewport[(500-int(X)):(500 + int(X)), int(Y)+500, 2] = RGB[0][2]
    else:
        while Trash <= 2*math.pi*R:
            Trash += 0.1
            X = R*math.cos(Trash)
            Y = R*math.sin(Trash)
            Viewport[int(X)+500, int(Y)+500, 1] = 255

    return Viewport

Img = Image.fromarray(Sphere(500, True))
Img = Img.resize((1000//2, 1000//2), resample=Image.ANTIALIAS)
Img.save("Max.png")
Img.show()

Window = tkinter.Tk()
Window.geometry('720x500')
ViewportFrame = tkinter.Frame(bg='black', cursor='plus', width=500, height=500, relief = tkinter.RIDGE)
ViewportFrame.grid(row = 0, column = 0, columnspan = 3, rowspan = 3)
ShapeFrame = tkinter.Frame(bg='white', cursor='plus', width=220, height=125, relief = tkinter.SUNKEN)
ShapeFrame.grid(row = 0, column = 4, columnspan = 1)
ButtonFrame = tkinter.Frame(bg='white', cursor='plus', width=220, height=125, relief = tkinter.SUNKEN)
ButtonFrame.grid(row = 1, column = 4, columnspan = 1)
ConfigureFrame = tkinter.Frame(bg='white', cursor='plus', width=220, height=125, relief = tkinter.SUNKEN)
ConfigureFrame.grid(row = 2, column = 4, columnspan = 1)
FinalFrame = tkinter.Frame(bg='white', cursor='plus', width=220, height=125, relief = tkinter.SUNKEN)
FinalFrame.grid(row = 3, column = 4, columnspan = 1)
Window.mainloop()
