from Tkinter import *
from time import *
from random import *
from math import *
import sys

class MyWindow(Frame):
    def __init__(self, master=None):
        self.bgcolor = "yellow"
        Frame.__init__(self, master)
        self.grid()
        top = self.winfo_toplevel()
        top.title("Basic Graphics")
        self.createWidgets()
        
    def createWidgets(self):
        MenuBar = Frame(self)
        MenuBar.grid(sticky=NW)
        self.makeFileMenu(MenuBar)

        # This label doesn't do anything; it is just here as a model.
        # Delete it if you don't need a label.
        global label
        label = Label(MenuBar, text="Label")
        label.grid(row=0, column = 1)

        # This scale is also here as a model.  You can get its value in
        # the scaleCallback function (near the bottom of the program),
        # or you can access scaleValue.get()
        global scaleValue
        scaleValue = IntVar()
        scale = Scale(MenuBar, from_=1, to=10, orient=HORIZONTAL,
                      variable = scaleValue, command=scaleCallback)
        scale.grid(row=0, column  = 2)

        # Here is a typical button.  When it is pushed, the buttonCallback
        # function (near the bottom of the program) is called.
        TestButton = Button(MenuBar, text="Button", command = buttonCallback)
        TestButton.grid(row = 0, column = 3)

        global canvas
        canvas = Canvas(self, width=500, height=500, background=self.bgcolor)
        canvas.grid(row=1)
        self.canvas = canvas
        
    def makeFileMenu(self, MB):
        File_button = Menubutton(MB, text='File', underline=0)
        File_button.menu = Menu(File_button)
        File_button['menu'] = File_button.menu
        File_button.grid(column = 0)

        File_button.menu.add_command(label='Quit', underline=0, command=self.quit)
        
class Shape:
    def __init__(self, vertices, color):
        self.color = color
        self.vertices = vertices
        self.my_shape = None
        
    def Moveto(self, a, b):
        # This moves the shape to point (a,b)
        [x, y] = self.vertices[0]
        d0 = a-x
        d1 = b-y
        self.Moveby(d0, d1)

    def Moveby(self, a, b):
        # This moves the shape a units horizontally and b units vertically
        canvas.move(self.my_shape, a, b)
        canvas.update()
        for v in self.vertices:
            v[0] = v[0] + a
            v[1] = v[1] + b

            
    def ChangeColor(self, color):
        # This changes the shape's color.  Possible colors include
        # "white", "black", "red", "green", "blue", "yellow", "cyan",
        # "magenta", "light green", etc.
        canvas.itemconfigure(self.my_shape, fill = color )
        canvas.update()
        self.color = color
        
    def Position(self):
        return (self.vertices[0][0], self.vertices[0][1])

    def Delete(self):
        canvas.delete(self.my_shape)

    def NextStep(self):
        self.Moveby(0, 1)
        
class Rectangle(Shape):
    def __init__(self, x, y, x1, y1, color):
        # This creates a square with corners (x, y) and (x1, y1)
        Shape.__init__(self, [[x, y], [x1, y1]], color)
        self.my_shape = canvas.create_rectangle(x, y, x1, y1, fill = color)                                               
                                               
class Oval(Shape):
    def __init__(self, x, y, hrad, vrad, color):
        # This creates an oval centered at (x, y) with horizontal radius
        # hrad and vertical radius vrad
        Shape.__init__(self, [[x-hrad, y-vrad], [x+hrad, y+vrad]], color)
        v0 = self.vertices[0]
        v1 = self.vertices[1]
        self.my_shape = canvas.create_oval(v0[0], v0[1], v1[0], v1[1], fill = color)

class Square(Rectangle):
    def __init__(self, x, y, side, color):
        # This creates a square with upper left corner at (x, y) and length side
        Rectangle.__init__(self, x, y, x+side, y+side, color)

class Circle(Oval):
    # This creates a circle centered at (x, y) with the given radius
    def __init__(self, x, y, radius, color):
        Oval.__init__(self, x, y, radius, radius, color)
        canvas.update()
             
def NewSquare():
    colors = ["red", "green", "blue", "yellow", "orange", "brown", "cyan", "magenta"]
    x = randint(1, 500)
    y = randint(1, 500)
    color = colors[ randint(0, len(colors)-1) ]
    s = Square( x, y, 30, color)
    AnimationList.append(s)
    
def NewCircle():
    colors = ["red", "green", "blue", "yellow", "orange", "brown", "cyan", "magenta"]
    x = randint(1, 500)
    y = randint(1, 500)
    color = colors[ randint(0, len(colors)-1) ]
    c = Circle( x, y, 20, color)
    AnimationList.append(c)
    
def buttonCallback():
    print "The button was pushed"

def scaleCallback(stringValue):
    n = int(stringValue)
    print "The scale was set to %d" % n

def AnimationLoop():
    # This calls NextStep on each object in the animation list.
    for object in AnimationList:
        object.NextStep()
    canvas.after(100, AnimationLoop)
        
def main():    
    global AnimationList
    AnimationList = []
    window = MyWindow()

    # As a demo, this makes a new square, circle, oval and rectangle.
    NewSquare()
    NewSquare()
    NewCircle()
    NewCircle()
    
    AnimationLoop()
    canvas.mainloop()

main()
